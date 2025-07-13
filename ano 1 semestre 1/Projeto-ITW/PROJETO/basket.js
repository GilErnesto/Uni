const basketballId = new URLSearchParams(window.location.search).get("id");

$(document).ready(function () {
    function VM() {
        var self = this;

        // URL da API de Basquete
        self.basketballAPI = `http://192.168.160.58/Paris2024/api/Basketballs/${basketballId}`;

        // Observables para armazenar dados do basquete
        self.basketballInfo = ko.observable({
            Id: '',
            Name: '',
            Date: '',
            EventId: '',
            EventName: '',
            StageId: '',
            StageName: '',
            Sex: '',
            Venue: '',
            ParticipantType: '',
            ParticipantCode: '',
            ParticipantName: '',
            CountryCode: '',
            CountryName: '',
            CountryFlag: '',
            NOCFlag: '',
            Rank: '',
            Result: '',
            ResultType: '',
            ResultIRM: '',
            ResultDiff: '',
            ResultWLT: '',
            QualificationMark: '',
            StartOrder: '',
            Bib: ''
        });

        // Função para buscar informações de basquete
        self.fetchBasketballInfo = function () {
            if (!basketballId) {
                console.error("Basketball ID não encontrado na URL.");
                return;
            }

            $.ajax({
                url: self.basketballAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados do basquete recebidos:", data);

                    // Atualiza os dados do basquete
                    self.basketballInfo({
                        Id: data.Id,
                        Name: data.Name,
                        Date: new Date(data.Date).toLocaleString(),
                        EventId: data.EventId,
                        EventName: data.EventName,
                        StageId: data.StageId,
                        StageName: data.StageName,
                        Sex: data.Sex,
                        Venue: data.Venue,
                        ParticipantType: data.ParticipantType,
                        ParticipantCode: data.ParticipantCode,
                        ParticipantName: data.ParticipantName,
                        CountryCode: data.CountryCode,
                        CountryName: data.CountryName,
                        CountryFlag: data.CountryFlag || '/PROJETO/imagens/FlagNotFound.png', // Imagem padrão se não houver flag
                        NOCFlag: data.NOCFlag,
                        Rank: data.Rank,
                        Result: data.Result,
                        ResultType: data.ResultType,
                        ResultIRM: data.ResultIRM,
                        ResultDiff: data.ResultDiff,
                        ResultWLT: data.ResultWLT,
                        QualificationMark: data.QualificationMark,
                        StartOrder: data.StartOrder,
                        Bib: data.Bib
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar informações de basquete: ${textStatus} - ${errorThrown}`);
                    // Configura a imagem de flag padrão em caso de erro na solicitação
                    self.basketballInfo().CountryFlag = '/PROJETO/imagens/FlagNotFound.png';
                }
            });
        };

        // Inicializa a busca
        self.fetchBasketballInfo();
    }

    // Cria e aplica o ViewModel
    var vm = new VM();
    ko.applyBindings(vm);
});