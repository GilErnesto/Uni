$(document).ready(function () {
    function VM() {
        console.log('ViewModel initiated...');
        var self = this;

        self.baseUri = ko.observable('http://192.168.160.58/Paris2024/API/Medals');
        console.log('BaseURI:', self.baseUri());
        self.displayName = 'Paris2024 Medalhas List';
        self.error = ko.observable('');
        self.passingMessage = ko.observable('');
        self.medals = ko.observableArray([]);
        self.allMedals = ko.observableArray([]);
        self.currentPage = ko.observable(1);
        self.pagesize = ko.observable(150); // Alterado para 150 medalhas por página
        self.totalRecords = ko.observable(1044);
        self.hasPrevious = ko.observable(false);
        self.hasNext = ko.observable(false);
        self.searchTerm = ko.observable('');
        self.order = ko.observable('');
        self.sortKey = ko.observable(''); // Chave de ordenação
        self.sortOrder = ko.observable('asc'); // Ordem de ordenação (ascendente ou descendente)

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
            var size = Math.min(self.totalPages(), 6);
            var step;
            if (size < 6 || self.currentPage() === 1) {
                step = 0;
            } else if (self.currentPage() >= self.totalPages() - 4) {
                step = self.totalPages() - 6;
            } else {
                step = Math.max(self.currentPage() - 5, 0);
            }

            for (var i = 1; i <= size; i++) {
                list.push(i + step);
            }
            return list;
        };

        //--- Page Events
        self.activate = function (id) {
            console.log('CALL: getMedals...');
            fetchAllMedals(id);
        };

        function fetchAllMedals(page = 1) {
            var composedUri = self.baseUri() + "?page=" + page + "&pageSize=" + self.pagesize();
            ajaxHelper(composedUri, 'GET').done(function (data) {
                console.log('Data fetched from API:', data);
                hideLoading();

                // Process and group medals by country
                var groupedMedals = data.Medals.reduce((acc, medal) => {
                    if (!acc[medal.CountryName]) {
                        acc[medal.CountryName] = {
                            CountryName: medal.CountryName,
                            CountryCode: medal.CountryCode,
                            Gold: 0,
                            Silver: 0,
                            Bronze: 0,
                            Total: 0
                        };
                    }
                    if (medal.MedalName.includes("Gold")) {
                        acc[medal.CountryName].Gold += 1;
                    } else if (medal.MedalName.includes("Silver")) {
                        acc[medal.CountryName].Silver += 1;
                    } else if (medal.MedalName.includes("Bronze")) {
                        acc[medal.CountryName].Bronze += 1;
                    }
                    acc[medal.CountryName].Total += 1;
                    return acc;
                }, {});

                // Merge grouped medals with existing ones
                self.allMedals.push(...Object.values(groupedMedals));

                console.log('Grouped Medals:', self.allMedals());

                if (data.HasNext) {
                    fetchAllMedals(page + 1); // Fetch next page recursively
                } else {
                    self.totalRecords(self.allMedals().length);
                    self.totalPages(Math.ceil(self.totalRecords() / self.pagesize()));
                    self.applyPagination(); // Apply pagination and filtering after fetching all data
                }
            }).fail(function (jqXHR, textStatus, errorThrown) {
                console.error("Error fetching medals: ", textStatus, errorThrown);
                console.error("Response: ", jqXHR.responseText);
            });
        }

        self.applyPagination = function () {
            var filtered = self.filterMedals();
            var sortedMedals = filtered.sort(dynamicSort(self.sortKey(), self.sortOrder()));
            var startIndex = (self.currentPage() - 1) * self.pagesize();
            var endIndex = startIndex + self.pagesize();
            self.medals(sortedMedals.slice(startIndex, endIndex));
        };

        self.sortBy = function (key) {
            self.sortKey(key);
            self.sortOrder(self.sortOrder() === 'asc' ? 'desc' : 'asc');
            self.applyPagination();
        };

        function dynamicSort(property, order) {
            var sortOrder = order === 'asc' ? 1 : -1;
            return function (a, b) {
                var result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
                return result * sortOrder;
            };
        }

        self.searchMedals = function (searchTerm, order) {
            console.log('CALL: searchMedals...');
            self.searchTerm(searchTerm);
            self.order(order);
            self.activate(1); // Reinicia a pesquisa na página 1
        };

        self.filterMedals = function () {
            var searchTerm = self.searchTerm().toLowerCase();
            if (!searchTerm) {
                return self.allMedals();
            }
            return ko.utils.arrayFilter(self.allMedals(), function (medal) {
                return medal.CountryName.toLowerCase().includes(searchTerm);
            });
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
    }

    var viewModel = new VM();
    ko.applyBindings(viewModel);

    $("#searchButton").click(function () {
        var searchTerm = $("#procura").val();
        var order = $("#orderSelect").val(); // Obtém o valor selecionado para a ordem
        if (searchTerm) {
            viewModel.searchMedals(searchTerm, order);
        }
    });

    $("#clearButton").click(function () {
        $("#procura").val('');
        viewModel.searchTerm('');
        viewModel.order('');
        viewModel.activate(1); // Recarrega a lista de medals sem filtro de pesquisa
    });
});

$(document).ajaxComplete(function (event, xhr, options) {
    $("#myModal").modal('hide');
});