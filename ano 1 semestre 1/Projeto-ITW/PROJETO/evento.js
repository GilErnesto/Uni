$(document).ready(function () {
    // Definindo sportId e name corretamente a partir da URL
    const sportId = new URLSearchParams(window.location.search).get("sportId");
    const name = new URLSearchParams(window.location.search).get("name");

    function VM() {
        var self = this;

        // Verifique se sportId e name foram passados na URL
        if (!sportId || !name) {
            console.error("sportId ou name não foram encontrados na URL");
            return;
        }

        // URL da API para obter as competições com base no sportId e name
        self.competitionAPI = `http://192.168.160.58/Paris2024/api/Competitions?sportId=${sportId}&name=${name}`;

        // Observáveis
        self.competition = ko.observable({
            Name: "Carregando...",
            Tag: "Carregando...",
            SportInfo: { Id: "", Name: "" } // Adicionando a propriedade SportInfo
        });
        self.athletes = ko.observableArray([]);
        self.athleteCount = ko.observable(0);

        // Função de log para depuração
        self.log = function (message) {
            console.log(`[VM Log]: ${message}`);
        };

        // Função para buscar as competições com base no sportId e name
        self.fetchCompetitions = function () {
            self.log("Fetching competitions...");
            $.ajax({
                url: self.competitionAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    self.log("Competitions fetched successfully.");
                    console.log("API Response:", data);

                    // Atualiza os dados da competição e atletas
                    if (data) {
                        self.competition({
                            Name: data.Name,
                            Tag: data.Tag,
                            SportInfo: { Id: data.SportInfo.Id, Name: data.SportInfo.Name }
                        });

                        // Atualiza a lista de atletas
                        self.athletes(data.Athletes);
                        self.athleteCount(data.Athletes.length);
                    } else {
                        self.competition({
                            Name: "Nenhuma competição encontrada",
                            Tag: "Nenhuma tag disponível",
                            SportInfo: { Id: "", Name: "" }
                        });
                        self.athletes([]);
                        self.athleteCount(0);
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    self.log(`Error fetching competitions: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Inicializa a busca
        self.fetchCompetitions();
    }

    // Aplica o binding do Knockout
    var vm = new VM();
    ko.applyBindings(vm);
});
