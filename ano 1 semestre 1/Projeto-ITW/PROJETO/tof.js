var vm = function () {
    console.log('ViewModel initiated...');
    var self = this;
    self.baseUri = ko.observable('http://192.168.160.58/Paris2024/api/Technical_officials');
    console.log('BaseURI:', self.baseUri());
    self.displayName = 'Paris2024 Technical Officials List';
    self.error = ko.observable('');
    self.passingMessage = ko.observable('');
    self.officials = ko.observableArray([]);
    self.filteredOfficials = ko.observableArray([]);
    self.currentPage = ko.observable(1);
    self.pagesize = ko.observable(50);
    self.totalRecords = ko.observable(0);
    self.hasPrevious = ko.observable(false);
    self.hasNext = ko.observable(false);
    self.searchTerm = ko.observable('');
    self.order = ko.observable('');

    // Computed observables for pagination
    self.previousPage = ko.computed(function () {
        return self.currentPage() - 1;
    }, self);
    self.nextPage = ko.computed(function () {
        return self.currentPage() + 1;
    }, self);
    self.fromRecord = ko.computed(function () {
        return self.previousPage() * self.pagesize() + 1;
    }, self);
    self.toRecord = ko.computed(function () {
        return Math.min(self.currentPage() * self.pagesize(), self.totalRecords());
    }, self);
    self.totalPages = ko.observable(0);
    self.pageArray = ko.computed(function () {
        var list = [];
        var size = Math.min(self.totalPages(), 9);
        var step;
        if (size < 9 || self.currentPage() === 1) {
            step = 0;
        } else if (self.currentPage() >= self.totalPages() - 4) {
            step = self.totalPages() - 9;
        } else {
            step = Math.max(self.currentPage() - 5, 0);
        }

        for (var i = 1; i <= size; i++) {
            list.push(i + step);
        }
        return list;
    });

    // Page Events
    self.activate = function (id) {
        console.log('CALL: getTechnicalOfficials...');
        var composedUri = self.baseUri() + "?page=" + id + "&pageSize=" + self.pagesize();
        if (self.searchTerm()) {
            composedUri += "&search=" + self.searchTerm();
        }
        if (self.order()) {
            composedUri += "&order=" + self.order();
        }
        ajaxHelper(composedUri, 'GET').done(function (data) {
            console.log(data);
            hideLoading();
            self.officials(data.Technical_officials);
            self.filteredOfficials(data.Technical_officials);

            self.currentPage(data.CurrentPage);
            self.hasNext(data.HasNext);
            self.hasPrevious(data.HasPrevious);
            self.pagesize(data.PageSize);
            self.totalPages(data.TotalPages);
            self.totalRecords(data.TotalOfficials);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.error("Error fetching technical officials: ", textStatus, errorThrown);
            console.error("Response: ", jqXHR.responseText);
            hideLoading();
        });
    };

    self.searchOfficials = function () {
        console.log('CALL: searchOfficials...');
        self.currentPage(1); // Reset to first page
        self.filteredOfficials([]); // Clear previous search results
        self.activate(1); // Start searching from the first page
    };

    self.clearFilter = function () {
        self.searchTerm('');
        self.order('');
        self.currentPage(1); // Reset to first page
        self.activate(1); // Recarrega a lista de oficiais sem filtro de pesquisa
    };

    self.onEnterSearch = function (d, e) {
        if ( e.keyCode === 13 ) {
            self.searchOfficials();
        }
        return true;
    };

    self.changePage = function (page) {
        self.currentPage(page);
        self.activate(page);
    };

    // Internal functions
    function ajaxHelper(uri, method, data) {
        self.error(''); // Clear error message
        return $.ajax({
            type: method,
            url: uri,
            dataType: 'json',
            contentType: 'application/json',
            data: data ? JSON.stringify(data) : null,
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("AJAX Call[" + uri + "] Fail...");
                hideLoading();
                self.error(errorThrown);
            }
        });
    }

    function showLoading() {
        $("#myModal").modal('show', {
            backdrop: 'static',
            keyboard: false
        });
    }

    function hideLoading() {
        $('#myModal').on('shown.bs.modal', function (e) {
            $("#myModal").modal('hide');
        });
    }

    function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;
        console.log("sPageURL=", sPageURL);
        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }
    }

    // Start
    showLoading();
    var pg = getUrlParameter('page');
    var search = getUrlParameter('search');
    var order = getUrlParameter('order');
    if (search) {
        self.searchTerm(search);
    }
    if (order) {
        self.order(order);
    }
    console.log(pg);
    if (pg == undefined) {
        self.activate(1);
    } else {
        self.activate(pg);
    }
    console.log("VM initialized!");
};

$(document).ready(function () {
    console.log("ready!");
    var viewModel = new vm();
    ko.applyBindings(viewModel);
    console.log(viewModel);

    $("#searchButton").click(function () {
        viewModel.searchOfficials();
    });

    $("#clearButton").click(function () {
        viewModel.clearFilter();
    });
});

$(document).ajaxComplete(function (event, xhr, options) {
    $("#myModal").modal('hide');
});