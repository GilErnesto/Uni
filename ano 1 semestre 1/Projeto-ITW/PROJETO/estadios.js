const athleteId = new URLSearchParams(window.location.search).get("id");

$(document).ready(function () {
    function VM() {
        var self = this;

        // URL da API
        self.apiURL = `http://192.168.160.58/Paris2024/api/Venues`;

        // Observables para armazenar dados das modalidades
        self.sportData = ko.observableArray([]);

        // Função para buscar dados das modalidades
        self.fetchSportData = function () {
            $.ajax({
                url: self.apiURL,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados das modalidades recebidos:", data);

                    // Atualiza os dados das modalidades
                    if (data && data.length > 0) {
                        self.sportData(data); // Preenche o array com todas as modalidades
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar dados da API: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Inicializa a busca
        self.fetchSportData();
    }

    // Cria e aplica o ViewModel
    var vm = new VM();
    ko.applyBindings(vm);
});
