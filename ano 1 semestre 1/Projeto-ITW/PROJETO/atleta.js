const athleteId = new URLSearchParams(window.location.search).get("id");

$(document).ready(function () {
    function VM() {
        var self = this;

        // URL da API do Atleta
        self.athleteAPI = `http://192.168.160.58/Paris2024/api/Athletes/${athleteId}`;

        // Observables para armazenar dados do atleta
        self.athleteInfo = ko.observable({
            id: '',
            name: '',
            shortName: '',
            tvName: '',
            birthCountry: '',
            birthDate: '',
            birthPlace: '',
            sex: '',
            photo: '',
            height: '',
            weight: '',
            function: '',
            country: '',
            nationality: '',
            residencePlace: '',
            residenceCountry: '',
            family: '',
            language: '',
            occupation: '',
            education: '',
            sportingRelatives: '',
            sports: [],       // Lista de esportes associados
            competitions: []  // Lista de competições associadas
        });

        // Função para buscar informações do atleta
        self.fetchAthleteInfo = function () {
            if (!athleteId) {
                console.error("Athlete ID não encontrado na URL.");
                return;
            }

            $.ajax({
                url: self.athleteAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados do atleta recebidos:", data);

                    // Atualiza os dados do atleta e ajusta o formato das competições
                    self.athleteInfo({
                        id: data.Id,
                        name: data.Name,
                        shortName: data.NameShort,
                        tvName: data.NameTV,
                        birthCountry: data.BirthCountry,
                        birthDate: data.BirthDate ? new Date(data.BirthDate).toLocaleDateString() : '',
                        birthPlace: data.BirthPlace,
                        sex: data.Sex,
                        photo: data.Photo || '/PROJETO/imagens/PersonNotFound.png', // Configura a imagem padrão se não houver imagem
                        height: data.Height,
                        weight: data.Weight,
                        function: data.Function,
                        country: data.Country,
                        nationality: data.Nationality_code,
                        residencePlace: data.Residence_place,
                        residenceCountry: data.Residence_country,
                        family: data.Family,
                        language: data.Lang,
                        occupation: data.Occupation,
                        education: data.Education,
                        sportingRelatives: data.SportingRelatives,
                        sports: data.Sports.map(sport => ({
                            id: sport.Id,
                            name: sport.Name
                        })) || [],
                        competitions: data.Competitions.map((comp, index) => ({
                            SportId: comp.SportId || "N/A",  // Valor padrão se SportId for indefinido
                            Name: comp.Name,
                            Tag: comp.Tag,
                            Id: `comp_${index}` // Gera um identificador único para cada competição
                        })) || []
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar informações do atleta: ${textStatus} - ${errorThrown}`);
                    // Configura a imagem padrão em caso de erro na solicitação
                    self.athleteInfo().photo = '/PROJETO/imagens/PersonNotFound.png';
                }
            });
        };

        // Inicializa a busca
        self.fetchAthleteInfo();
    }

    // Cria e aplica o ViewModel
    var vm = new VM();
    ko.applyBindings(vm);
});