$(document).ready(function () {

    function VM() {
        var self = this;

        // APIs
        self.modalityApiUrl = 'http://192.168.160.58/Paris2024/api/Sports';
        self.competitionApiUrl = 'http://192.168.160.58/Paris2024/api/Competitions';

        // Observables
        self.modalities = ko.observableArray([]);  // Lista de modalidades
        self.competitions = ko.observableArray([]);  // Lista de competições

        // Log Helper
        self.log = function (message) {
            console.log(`[VM Log]: ${message}`);
        };

        // Função para carregar os dados da API de modalidades
        self.loadModalityData = function () {
            $.ajax({
                url: self.modalityApiUrl,
                method: 'GET',
                success: function (data) {
                    if (Array.isArray(data) && data.length > 0) {
                        var modalitiesList = data.map(function (modality) {
                            return {
                                name: modality.Name,          // Nome da modalidade
                                pictogram: modality.Pictogram, // Pictograma da modalidade
                                id: modality.Id               // ID da modalidade
                            };
                        });
                        self.modalities(modalitiesList);
                    } else {
                        self.log('Nenhuma modalidade encontrada.');
                    }
                },
                error: function () {
                    self.log('Erro ao carregar os dados da API de modalidades.');
                }
            });
        };

        // Função para carregar competições para uma modalidade específica
        self.loadCompetitionsForModality = function (modalityId) {
            const competitionUrl = `${self.competitionApiUrl}?page=1&pagesize=1000&modalityId=${modalityId}`;  // pageSize aumentado

            $.ajax({
                url: competitionUrl,
                method: 'GET',
                success: function (data) {
                    if (data && Array.isArray(data.Competitions) && data.Competitions.length > 0) {
                        // Filtra as competições pela modalidade (caso a API retorne mais competições do que o necessário)
                        var competitionList = data.Competitions.filter(function (competition) {
                            return competition.SportId === modalityId;  // Filtra para garantir que só competições da modalidade selecionada
                        }).map(function (competition) {
                            return {
                                sportId: competition.SportId,
                                name: competition.Name,
                                tag: competition.Tag
                            };
                        });
                        self.competitions(competitionList);

                        // Remove o atributo "hidden" da tabela para exibir as competições
                        $('#competitionTable').removeAttr('hidden');
                    } else {
                        self.log('Nenhuma competição encontrada para a modalidade.');
                        self.competitions([]); // Limpa a tabela se não houver competições
                        $('#competitionTable').attr('hidden', 'true'); // Mantém a tabela oculta se não houver competições
                    }
                },
                error: function () {
                    self.log('Erro ao carregar as competições para a modalidade.');
                }
            });
        };




        // Inicializa os dados
        self.loadModalityData();
    }

    // Cria uma instância do VM e aplica o Knockout.js
    var vm = new VM();
    ko.applyBindings(vm);

});
