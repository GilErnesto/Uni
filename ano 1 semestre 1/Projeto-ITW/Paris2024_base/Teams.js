// JavaScript source code
// ViewModel KnockOut v6
// ViewModel KnockOut
var vm = function () {
    console.log('ViewModel initiated...');
    var self = this;
    // Base URI for the API (Substitua pela URI da API de equipes)
    self.baseUri = ko.observable('http://192.168.160.58/Paris2024/API/athletes');
    console.log('BaseURI');
    self.displayName = 'Paris2024 Athletes List'; // Substitua pelo nome apropriado para equipes
    self.error = ko.observable('');
    self.passingMessage = ko.observable('');
    self.athletes = ko.observableArray([]); // Substitua por self.teams
    self.currentPage = ko.observable(1);
    self.pagesize = ko.observable(20);
    self.totalRecords = ko.observable(50);
    self.hasPrevious = ko.observable(false);
    self.hasNext = ko.observable(false);
    self.searchTerm = ko.observable('');
    self.order = ko.observable('');

    self.previousPage = ko.computed(function () {
        return self.currentPage() * 1 - 1;
    }, self);
    self.nextPage = ko.computed(function () {
        return self.currentPage() * 1 + 1;
    }, self);
    self.fromRecord = ko.computed(function () {
        return self.previousPage() * self.pagesize() + 1;
    }, self);
    self.toRecord = ko.computed(function () {
        return Math.min(self.currentPage() * self.pagesize(), self.totalRecords());
    }, self);
    self.totalPages = ko.observable(0);
    self.pageArray = function () {
        var list = [];
        var size = Math.min(self.totalPages(), 9);
        var step;
        if (size < 9 || self.currentPage() === 1)
            step = 0;
        else if (self.currentPage() >= self.totalPages() - 4)
            step = self.totalPages() - 9;
        else
            step = Math.max(self.currentPage() - 5, 0);

        for (var i = 1; i <= size; i++)
            list.push(i + step);
        return list;
    };

    //--- Page Events
    self.activate = function (id) {
        console.log('CALL: getAthletes...'); // Substitua por getTeams
        // Composed URI for the API call (Substitua pela URI da API de equipes)
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
            self.athletes(data.Athletes); // Substitua por self.teams(data.Teams)

            self.currentPage(data.CurrentPage);
            self.hasNext(data.HasNext);
            self.hasPrevious(data.HasPrevious);
            self.pagesize(data.PageSize);
            self.totalPages(data.TotalPages);
            self.totalRecords(data.TotalAthletes); // Substitua por data.TotalTeams
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.error("Error fetching athletes: ", textStatus, errorThrown); // Substitua por teams
            console.error("Response: ", jqXHR.responseText);
        });
    };

    self.searchAthletes = function (searchTerm, order) { // Substitua por searchTeams
        console.log('CALL: searchAthletes...'); // Substitua por searchTeams
        self.searchTerm(searchTerm);
        self.order(order);
        self.activate(1); // Reinicia a pesquisa na p�gina 1
    };

    //--- Internal functions
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

    function sleep(milliseconds) {
        const start = Date.now();
        while (Date.now() - start < milliseconds);
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

    //--- start ....
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
    $('#myModal').on('show.bs.modal', function () {
        $(this).removeAttr('aria-hidden');
    });

    $('#myModal').on('hidden.bs.modal', function () {
        $(this).attr('aria-hidden', 'true');
        if (typeof lastFocusedElement !== 'undefined') {
            lastFocusedElement.focus();
        }
    });

    var lastFocusedElement;
    $('#myModal').on('show.bs.modal', function () {
        lastFocusedElement = document.activeElement;
    });

    $("#searchButton").click(function () {
        var searchTerm = $("#procura").val();
        var order = $("#orderSelect").val(); // Obt�m o valor selecionado para a ordem
        if (searchTerm) {
            viewModel.searchAthletes(searchTerm, order); // Substitua por searchTeams
        }
    });

    $("#clearButton").click(function () {
        $("#procura").val('');
        viewModel.searchTerm('');
        viewModel.order('');
        viewModel.activate(1); // Recarrega a lista de equipes sem filtro de pesquisa
    });
});

$(document).ajaxComplete(function (event, xhr, options) {
    $("#myModal").modal('hide');
});