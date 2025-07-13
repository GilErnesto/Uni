$(document).ready(function () {
    function VM() {
        var self = this;

        // API URL
        self.apiURL = "http://192.168.160.58/Paris2024/api/Coaches";

        // Observables
        self.displayName = ko.observable("Lista de Treinadores Galeria");
        self.coaches = ko.observableArray([]);
        self.currentPage = ko.observable(1);
        self.pageSize = ko.observable(50);
        self.totalPages = ko.observable(0);
        self.hasPrevious = ko.observable(false);
        self.hasNext = ko.observable(false);
        self.searchTerm = ko.observable('');
        self.order = ko.observable(1); // 1: Name, 2: Function, etc.
        self.totalRecords = ko.observable(0);

        // Computed Observables
        self.previousPage = ko.computed(() => self.currentPage() - 1);
        self.nextPage = ko.computed(() => self.currentPage() + 1);
        self.fromRecord = ko.computed(() => (self.currentPage() - 1) * self.pageSize() + 1);
        self.toRecord = ko.computed(() => Math.min(self.currentPage() * self.pageSize(), self.totalRecords()));

        // Computed array for pagination
        self.pageArray = ko.computed(() => {
            let pages = [];
            for (let i = 1; i <= self.totalPages(); i++) {
                pages.push(i);
            }
            return pages;
        });

        // Fetch coaches
        self.fetchCoaches = function (page) {
            const url = `${self.apiURL}?page=${page}&pageSize=${self.pageSize()}&search=${self.searchTerm()}&order=${self.order()}`;
            $.ajax({
                url: url,
                method: "GET",
                dataType: "json",
                success: function (data) {
                    console.log("Coaches fetched:", data);
                    if (data && data.Coaches) {
                        self.coaches(data.Coaches);
                        self.currentPage(data.CurrentPage);
                        self.totalPages(data.TotalPages);
                        self.hasPrevious(data.HasPrevious);
                        self.hasNext(data.HasNext);
                        self.totalRecords(data.TotalCoaches);
                    }
                },
                error: function (xhr, status, error) {
                    console.error("Failed to fetch coaches:", status, error);
                },
            });
        };

        // Navigate to previous page
        self.prevPage = function () {
            if (self.hasPrevious()) {
                self.fetchCoaches(self.previousPage());
            }
        };

        // Navigate to next page
        self.nextPage = function () {
            if (self.hasNext()) {
                self.fetchCoaches(self.nextPage());
            }
        };

        // Handle search
        self.searchCoaches = function () {
            self.fetchCoaches(1); // Reset to first page on search
        };

        // Clear search
        self.clearSearch = function () {
            self.searchTerm('');
            self.fetchCoaches(1); // Reset to first page
        };

        // Initialize
        self.fetchCoaches(self.currentPage());
    }

    // Apply Knockout.js bindings
    var vm = new VM();
    ko.applyBindings(vm);

    // Button handlers for search and clear
    $("#searchButton").click(() => vm.searchCoaches());
    $("#clearButton").click(() => vm.clearSearch());
});