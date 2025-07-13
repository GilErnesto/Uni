$(document).ready(function () {

    function VM() {
        var self = this;

        // API
        self.modalityApiUrl = 'http://192.168.160.58/Paris2024/api/Sports';

        // Observables
        self.modalities = ko.observableArray([]);  // Lista de modalidades

        // Log Helper
        self.log = function (message) {
            console.log(`[VM Log]: ${message}`);
        };

        // Função para carregar os dados da API
        self.loadModalityData = function () {
            $.ajax({
                url: self.modalityApiUrl,
                method: 'GET',
                success: function (data) {
                    // Verifica se os dados foram carregados corretamente
                    if (Array.isArray(data) && data.length > 0) {
                        // Mapeia os dados para a estrutura desejada
                        var modalitiesList = data.map(function (modality) {
                            return {
                                name: modality.Name,          
                                pictogram: modality.Pictogram,
                                id: modality.Id               
                            };
                        });

                        // Atualiza a lista de modalidades com os novos dados
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

        // Carrega os dados assim que o VM for instanciado
        self.loadModalityData();
    }

    // Cria uma instância do VM e aplica o Knockout.js
    var vm = new VM();
    ko.applyBindings(vm);

});
