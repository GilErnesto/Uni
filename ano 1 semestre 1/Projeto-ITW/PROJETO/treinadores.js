﻿//v7
// ViewModel KnockOut
// ViewModel KnockOut
var vm = function () {
    console.log('ViewModel initiated...');
    var self = this;
    self.baseUri = ko.observable('http://192.168.160.58/Paris2024/API/Coaches');
    console.log('BaseURI');
    self.displayName = 'Lista de Treinadores';
    self.error = ko.observable('');
    self.passingMessage = ko.observable('');
    self.coaches = ko.observableArray([]);
    self.currentPage = ko.observable(1);
    self.pagesize = ko.observable(20); // Certifique-se de que está usando "pagesize" em vez de "pageSize"
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
        console.log('CALL: getCoaches...');
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
            self.coaches(data.Coaches);

            self.currentPage(data.CurrentPage);
            self.hasNext(data.HasNext);
            self.hasPrevious(data.HasPrevious);
            self.pagesize(data.PageSize);
            self.totalPages(data.TotalPages);
            self.totalRecords(data.TotalCoaches);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.error("Error fetching coaches: ", textStatus, errorThrown);
            console.error("Response: ", jqXHR.responseText);
        });
    };

    self.searchCoaches = function (searchTerm, order) {
        console.log('CALL: searchCoaches...');
        self.searchTerm(searchTerm);
        self.order(order);
        self.activate(1); // Reinicia a pesquisa na página 1
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
        var order = $("#orderSelect").val(); // Obtém o valor selecionado para a ordem
        if (searchTerm) {
            viewModel.searchCoaches(searchTerm, order);
        }
    });

    $("#clearButton").click(function () {
        $("#procura").val('');
        viewModel.searchTerm('');
        viewModel.order('');
        viewModel.activate(1); // Recarrega a lista de treinadores sem filtro de pesquisa
    });
});

$(document).ajaxComplete(function (event, xhr, options) {
    $("#myModal").modal('hide');
});