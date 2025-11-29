#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <string.h>

/* SUGESTÂO: utilize as páginas do manual para conhecer mais sobre as funções
  usadas: man opendir man readdir
*/

void listDir(char dirname[]) {
  DIR *dp;
  struct dirent *dent;

  dp = opendir(dirname);
  if (dp == NULL) {
    perror("Error opening directory");
    return;
  }

  dent = readdir(dp);
  while (dent != NULL) {
    if (dent->d_name[0] != '.') /* do not list hidden dirs/files */
    {
      struct stat path_stat;
      char fullPath[1024];
      snprintf(fullPath, sizeof(fullPath), "%s/%s", dirname, dent->d_name);
      
      if (stat(fullPath, &path_stat) != 0) {
        perror("Error executing stat");
        return;
      }

      char type = ' ';
      if (S_ISDIR(path_stat.st_mode))
        type = 'd';

      printf("%c %s/%s\n", type, dirname, dent->d_name);
    }

    dent = readdir(dp);
  }
  
  closedir(dp);
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s base_directory\n", argv[0]);
    return EXIT_FAILURE;
  }

  listDir(argv[1]);

  return EXIT_SUCCESS;
}