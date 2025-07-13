$(document).ready(function () {
    function VM() {
        var self = this;

        // API URL
        self.apiURL = "http://192.168.160.58/Paris2024/api/Athletes";

        // Observables
        self.displayName = ko.observable("Lista de Atletas Galeria");
        self.Athletes = ko.observableArray([]);
        self.currentPage = ko.observable(1);
        self.pageSize = ko.observable(50);
        self.totalPages = ko.observable(0);
        self.hasPrevious = ko.observable(false);
        self.hasNext = ko.observable(false);
        self.searchTerm = ko.observable('');
        self.order = ko.observable(1); // 1: Name, 2: Function, etc.
        self.totalRecords = ko.observable(11110);

        // Computed Observables
        self.previousPage = ko.computed(() => self.currentPage() - 1);
        self.nextPage = ko.computed(() => self.currentPage() + 1);
        self.fromRecord = ko.computed(() => (self.currentPage() - 1) * self.pageSize() + 1);
        self.toRecord = ko.computed(() => Math.min(self.currentPage() * self.pageSize(), self.totalRecords()));

        // Page Array for pagination
        self.pageArray = ko.computed(function () {
            var pages = [];
            var startPage = Math.max(1, self.currentPage() - 4);
            var endPage = Math.min(self.totalPages(), self.currentPage() + 4);

            for (var i = startPage; i <= endPage; i++) {
                pages.push(i);
            }
            return pages;
        });

        // Fetch Athletes
        self.fetchAthletes = function (page) {
            const url = `${self.apiURL}?page=${page}&pageSize=${self.pageSize()}&search=${self.searchTerm()}&order=${self.order()}`;
            $.ajax({
                url: url,
                method: "GET",
                dataType: "json",
                success: function (data) {
                    console.log("Athletes fetched:", data);
                    if (data && data.Athletes) {
                        self.Athletes(data.Athletes);
                        self.currentPage(data.CurrentPage);
                        self.totalPages(data.TotalPages);
                        self.hasPrevious(data.HasPrevious);
                        self.hasNext(data.HasNext);
                        self.totalRecords(data.TotalAthletes);
                    }
                },
                error: function (xhr, status, error) {
                    console.error("Failed to fetch Athletes:", status, error);
                },
            });
        };

        // Navigate to previous page
        self.prevPage = function () {
            if (self.hasPrevious()) {
                self.fetchAthletes(self.previousPage());
            }
        };

        // Navigate to next page
        self.nextPage = function () {
            if (self.hasNext()) {
                self.fetchAthletes(self.nextPage());
            }
        };

        // Handle search
        self.searchAthletes = function () {
            self.fetchAthletes(1); // Reset to first page on search
        };

        // Clear search
        self.clearSearch = function () {
            self.searchTerm('');
            self.fetchAthletes(1); // Reset to first page
        };

        // Initialize
        self.fetchAthletes(self.currentPage());
    }

    // Apply Knockout.js bindings
    var vm = new VM();
    ko.applyBindings(vm);

    // Button handlers for search and clear
    $("#searchButton").click(() => vm.searchAthletes());
    $("#clearButton").click(() => vm.clearSearch());
});