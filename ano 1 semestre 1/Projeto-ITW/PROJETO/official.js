const officialId = new URLSearchParams(window.location.search).get("id");

$(document).ready(function () {
    function VM() {
        var self = this;

        // URL da API do Oficial Técnico
        self.officialAPI = `http://192.168.160.58/Paris2024/api/Technical_officials/${officialId}`;

        // Observables para armazenar dados do oficial técnico
        self.officialInfo = ko.observable({
            id: '',
            name: '',
            sex: '',
            birthDate: '',
            photo: '',
            category: '',
            function: '',
            organisationCode: '',
            organisation: '',
            organisationLong: '',
            url: '',
            sports: []       // Lista de esportes associados
        });

        // Função para buscar informações do oficial técnico
        self.fetchOfficialInfo = function () {
            if (!officialId) {
                console.error("Official ID não encontrado na URL.");
                return;
            }

            $.ajax({
                url: self.officialAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados do oficial técnico recebidos:", data);

                    // Verifica se 'Sports' está presente e não é null antes de usar 'map'
                    const sports = data.Sports ? data.Sports.map(sport => ({
                        id: sport.Id,
                        name: sport.Name,
                        sportUrl: sport.Sport_url,
                        pictogram: sport.Pictogram,
                        athletes: sport.Athletes,
                        coaches: sport.Coaches,
                        competitions: sport.Competitions,
                        teams: sport.Teams,
                        technicalOfficials: sport.Technical_officials,
                        venues: sport.Venues
                    })) : [];

                    // Atualiza os dados do oficial técnico e ajusta o formato dos esportes
                    self.officialInfo({
                        id: data.Id,
                        name: data.Name,
                        sex: data.Sex,
                        birthDate: data.BirthDate ? new Date(data.BirthDate).toLocaleDateString() : '',
                        photo: data.Photo || '/PROJETO/imagens/PersonNotFound.png', // Configura a imagem padrão se não houver imagem
                        category: data.Category,
                        function: data.Function,
                        organisationCode: data.OrganisationCode,
                        organisation: data.Organisation,
                        organisationLong: data.OrganisationLong,
                        url: data.Url,
                        sports: sports
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar informações do oficial técnico: ${textStatus} - ${errorThrown}`);
                    // Configura a imagem padrão em caso de erro na solicitação
                    self.officialInfo().photo = '/PROJETO/imagens/PersonNotFound.png';
                }
            });
        };

        // Inicializa a busca
        self.fetchOfficialInfo();
    }

    // Cria e aplica o ViewModel
    var vm = new VM();
    ko.applyBindings(vm);
});