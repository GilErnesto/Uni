$(document).ready(function () {
    function VM() {
        var self = this;

        self.eventsAPI = 'http://192.168.160.58/Paris2024/api/Basketballs/Events';
        self.filterAPI = 'http://192.168.160.58/Paris2024/api/Basketballs';

        self.events = ko.observableArray([]);
        self.stages = ko.observableArray([]);
        self.basketballData = ko.observableArray([]);
        self.selectedEvent = ko.observable('');
        self.selectedStage = ko.observable('');

        self.currentPage = ko.observable(1);
        self.pagesize = ko.observable(1000);
        self.totalRecords = ko.observable(0);

        self.previousPage = ko.computed(function () {
            return self.currentPage() - 1;
        }, self);
        self.nextPage = ko.computed(function () {
            return self.currentPage() + 1;
        }, self);
        self.totalPages = ko.computed(function () {
            return Math.ceil(self.totalRecords() / self.pagesize());
        }, self);
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

        // Adicionando observáveis para searchTerm e order com valores padrão
        self.searchTerm = ko.observable('');
        self.order = ko.observable('');

        self.fetchEvents = function () {
            return $.ajax({
                url: self.eventsAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    self.events(data);
                    // Set default event selection
                    if (data.length > 0) {
                        self.selectedEvent(data[0].EventId);
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Error fetching events: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        self.fetchBasketballData = function () {
            var eventId = self.selectedEvent();
            var stageId = self.selectedStage() || '';

            var url = `${self.filterAPI}?EventId=${eventId}&StageId=${stageId}`;
            return $.ajax({
                url: url,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    self.basketballData(data);
                    self.totalRecords(data.length);
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Error fetching basketball data: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        self.updateStages = function () {
            var selectedEvent = self.events().find(event => event.EventId === self.selectedEvent());
            if (selectedEvent) {
                self.stages(selectedEvent.Stages);
                // Set default stage selection
                self.selectedStage('');
            } else {
                self.stages([]);
            }
        };

        self.selectedEvent.subscribe(function () {
            self.updateStages();
            self.fetchBasketballData();
        });

        self.selectedStage.subscribe(function () {
            self.fetchBasketballData();
        });

        // Inicializa a busca de eventos
        self.fetchEvents().then(function () {
            if (self.selectedEvent()) {
                self.updateStages();
                self.fetchBasketballData();
            }
        });
    }

    // Cria e aplica o ViewModel
    var vm = new VM();
    ko.applyBindings(vm);
});