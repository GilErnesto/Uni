#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <getopt.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>

#define MAX_PATH 1024

void list_directory(const char *dir_path, int files_only, int dirs_only, const char *extension);
void print_usage(const char *program_name);
int has_extension(const char *filename, const char *ext);

int main(int argc, char *argv[])
{
    int opt;
    int option_index = 0;
    int files_only = 0;
    int dirs_only = 0;
    char *extension = NULL;
    
    /* Define long options */
    static struct option long_options[] = {
        {"file",      no_argument,       0, 'f'},
        {"dir",       no_argument,       0, 'd'},
        {"ext",       required_argument, 0, 'e'},
        {"help",      no_argument,       0, 'h'},
        {0,           0,                 0,  0 }
    };
    
    /* Parse command line options */
    while ((opt = getopt_long(argc, argv, "fde:h", long_options, &option_index)) != -1)
    {
        switch (opt)
        {
            case 'f':
                files_only = 1;
                break;
            case 'd':
                dirs_only = 1;
                break;
            case 'e':
                extension = optarg;
                break;
            case 'h':
                print_usage(argv[0]);
                exit(EXIT_SUCCESS);
            default: /* '?' */
                print_usage(argv[0]);
                exit(EXIT_FAILURE);
        }
    }
    
    /* Check for conflicting options */
    if (files_only && dirs_only)
    {
        fprintf(stderr, "Error: Cannot use -f and -d options together\n");
        print_usage(argv[0]);
        exit(EXIT_FAILURE);
    }
    
    /* If extension is specified, force files_only mode */
    if (extension != NULL)
    {
        files_only = 1;
        dirs_only = 0;
    }
    
    /* If no directories specified, use current directory */
    if (optind >= argc)
    {
        printf("Listing contents of current directory:\n");
        list_directory(".", files_only, dirs_only, extension);
    }
    else
    {
        /* Process each specified directory */
        for (int i = optind; i < argc; i++)
        {
            if (argc - optind > 1)
            {
                printf("\n=== Directory: %s ===\n", argv[i]);
            }
            list_directory(argv[i], files_only, dirs_only, extension);
        }
    }
    
    return EXIT_SUCCESS;
}

void list_directory(const char *dir_path, int files_only, int dirs_only, const char *extension)
{
    DIR *dir;
    struct dirent *entry;
    struct stat file_stat;
    char full_path[MAX_PATH];
    int count = 0;
    
    /* Open directory */
    dir = opendir(dir_path);
    if (dir == NULL)
    {
        perror("Error opening directory");
        return;
    }
    
    /* Read directory entries */
    while ((entry = readdir(dir)) != NULL)
    {
        /* Skip . and .. entries */
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;
            
        /* Build full path for stat() */
        snprintf(full_path, sizeof(full_path), "%s/%s", dir_path, entry->d_name);
        
        /* Get file information */
        if (stat(full_path, &file_stat) == -1)
        {
            fprintf(stderr, "Error getting info for %s: %s\n", entry->d_name, strerror(errno));
            continue;
        }
        
        /* Apply filters based on options */
        if (S_ISDIR(file_stat.st_mode))
        {
            /* It's a directory */
            if (!files_only && (dirs_only || (!dirs_only && !files_only)))
            {
                printf("[DIR]  %s\n", entry->d_name);
                count++;
            }
        }
        else if (S_ISREG(file_stat.st_mode))
        {
            /* It's a regular file */
            if (!dirs_only && (files_only || (!dirs_only && !files_only)))
            {
                /* Check extension filter if specified */
                if (extension == NULL || has_extension(entry->d_name, extension))
                {
                    printf("[FILE] %s\n", entry->d_name);
                    count++;
                }
            }
        }
    }
    
    closedir(dir);
    
    /* Print summary */
    if (count == 0)
    {
        if (extension != NULL)
            printf("No files with extension '.%s' found.\n", extension);
        else if (files_only)
            printf("No files found.\n");
        else if (dirs_only)
            printf("No directories found.\n");
        else
            printf("Directory is empty.\n");
    }
    else
    {
        printf("\nTotal items listed: %d\n", count);
    }
}

int has_extension(const char *filename, const char *ext)
{
    char *dot = strrchr(filename, '.');
    if (dot == NULL)
        return 0; /* No extension */
    
    return strcmp(dot + 1, ext) == 0;
}

void print_usage(const char *program_name)
{
    printf("Usage: %s [OPTIONS] [DIRECTORY...]\n", program_name);
    printf("List directory contents with filtering options.\n\n");
    printf("Options:\n");
    printf("  -f, --file      List only files\n");
    printf("  -d, --dir       List only directories\n");
    printf("  -e, --ext EXT   List only files with extension EXT\n");
    printf("                  (implies -f option)\n");
    printf("  -h, --help      Show this help message\n\n");
    printf("If no directory is specified, current directory is used.\n");
    printf("Multiple directories can be specified.\n\n");
    printf("Examples:\n");
    printf("  %s                        # List all items in current directory\n", program_name);
    printf("  %s -f                     # List only files in current directory\n", program_name);
    printf("  %s --file                 # Same as -f\n", program_name);
    printf("  %s -d /home /tmp          # List only directories in /home and /tmp\n", program_name);
    printf("  %s --dir /home            # Same as -d /home\n", program_name);
    printf("  %s -e txt /home           # List only .txt files in /home\n", program_name);
    printf("  %s --ext c .              # List only .c files in current directory\n", program_name);
}