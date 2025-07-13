$(document).ready(function () {
    function ViewModel() {
        var self = this;

        self.baseUri = ko.observable('http://192.168.160.58/Paris2024/api/Teams');
        self.displayName = 'Lista de Equipas';
        self.error = ko.observable('');
        self.teams = ko.observableArray([]);
        self.filteredTeams = ko.observableArray([]);
        self.allTeams = ko.observableArray([]); // Adicionado para armazenar todas as equipes
        self.currentPage = ko.observable(1);
        self.pagesize = ko.observable(50); // Alterado para 50 equipes por página
        self.totalRecords = ko.observable(0);
        self.hasPrevious = ko.observable(false);
        self.hasNext = ko.observable(false);
        self.searchTerm = ko.observable('');
        self.order = ko.observable('');
        self.selectedSport = ko.observable(''); // Observable para o esporte selecionado

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

        // Eventos da página
        self.activate = function (id) {
            console.log('CALL: getTeams...');
            self.allTeams([]); // Limpar allTeams antes de buscar novos dados
            fetchAllTeams();
        };
        
        function fetchAllTeams(page = 1) {
            var uri = self.baseUri() + "?page=" + page + "&pageSize=" + self.pagesize();
            ajaxHelper(uri, 'GET').done(function (data) {
                self.allTeams.push(...data.Teams); // Adicionar ao allTeams
                if (data.HasNext) {
                    fetchAllTeams(page + 1); // Buscar próxima página
                } else {
                    self.totalRecords(self.allTeams().length);
                    self.totalPages(Math.ceil(self.totalRecords() / self.pagesize()));
                    self.applyPagination(); // Aplicar paginação e filtro
                }
            }).fail(function (jqXHR, textStatus, errorThrown) {
                console.error("Error fetching teams: ", textStatus, errorThrown);
                console.error("Response: ", jqXHR.responseText);
            });
        }

        self.applyPagination = function () {
            var startIndex = (self.currentPage() - 1) * self.pagesize();
            var endIndex = startIndex + self.pagesize();
            self.teams(self.allTeams().slice(startIndex, endIndex));
            self.filterTeams(); // Filtrar equipes após buscar
        };

        self.searchTeams = function () {
            console.log('CALL: searchTeams...');
            self.activate(1); // Reiniciar busca na página 1
        };

        // Filtrar equipes com base no esporte selecionado e no termo de busca
        self.filterTeams = function () {
            var sport = self.selectedSport();
            var searchTerm = self.searchTerm().toLowerCase();
            var filtered = ko.utils.arrayFilter(self.allTeams(), function (team) {
                var matchesSport = !sport || team.Sport_Codes === sport;
                var matchesSearch = !searchTerm || team.Name.toLowerCase().includes(searchTerm);
                return matchesSport && matchesSearch;
            });
            self.filteredTeams(filtered.slice((self.currentPage() - 1) * self.pagesize(), self.currentPage() * self.pagesize()));
        };

        // Limpar filtro
        self.clearFilter = function () {
            self.selectedSport('');
            self.searchTerm('');
            self.filterTeams();
        };

        // Funções internas
        function ajaxHelper(uri, method, data) {
            self.error(''); // Limpar mensagem de erro
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

        self.onEnterSearch = function (data, event) {
            if (event.keyCode === 13) { // Tecla Enter pressionada
                self.searchTeams();
            }
            return true;
        };

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

        // Carregamento inicial
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
    }

    var viewModel = new ViewModel(); // Definindo viewModel no escopo global
    ko.applyBindings(viewModel);

    $("#procura").keypress(function (e) {
        if (e.which == 13) { // Tecla Enter pressionada
            $("#searchButton").click();
        }
    });

    $("#searchButton").click(function () {
        var searchTerm = $("#procura").val();
        viewModel.searchTerm(searchTerm);
        viewModel.searchTeams();
    });

    $("#clearButton").click(function () {
        $("#procura").val('');
        viewModel.searchTerm('');
        viewModel.selectedSport('');
        viewModel.clearFilter();
        viewModel.activate(1); // Recarregar lista de equipes sem filtro de busca
    });

    $("#disciplines_code").change(function () {
        viewModel.selectedSport($(this).val());
        viewModel.filterTeams();
    });
});