const venueId = new URLSearchParams(window.location.search).get("id");

// Adicione sua chave de API do OpenWeatherMap aqui
const OPENWEATHERMAP_API_KEY = 'b2b1df463182c3cca5276e9d3267cc95';

$(document).ready(function () {
    function VM() {
        var self = this;

        // URL da API do Local (Venue)
        self.venueAPI = `http://192.168.160.58/Paris2024/api/Venues/${venueId}`;

        // URL da API do Esporte
        self.sportAPI = `http://192.168.160.58/Paris2024/api/Sports/`;

        // Observables para armazenar dados do local e do esporte
        self.venueInfo = ko.observable({
            id: '',
            name: '',
            dateStart: '',
            dateEnd: '',
            tag: '',
            url: '',
            lat: '',
            lon: '',
            sports: [], // Lista de esportes associados ao local
            weather: null // Dados do tempo
        });

        // Função para buscar informações do local
        self.fetchVenueInfo = function () {
            if (!venueId) {
                console.error("Venue ID não encontrado na URL.");
                return;
            }

            $.ajax({
                url: self.venueAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados do local recebidos:", data);

                    // Atualiza os dados do local
                    self.venueInfo({
                        id: data.Id,
                        name: data.Name,
                        dateStart: data.DateStart ? new Date(data.DateStart).toLocaleString() : '',
                        dateEnd: data.DateEnd ? new Date(data.DateEnd).toLocaleString() : '',
                        tag: data.Tag,
                        url: data.Url,
                        lat: data.Lat,
                        lon: data.Lon,
                        sports: [],  // Inicializa a lista de esportes
                        weather: null // Inicializa os dados do tempo
                    });

                    // Busca informações do tempo
                    self.fetchWeatherInfo(data.Lat, data.Lon);

                    // Itera sobre os esportes e busca as informações de cada um
                    if (data.Sports && data.Sports.length > 0) {
                        data.Sports.forEach(function (sport) {
                            self.fetchSportInfo(sport);
                        });
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar informações do local: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Função para buscar informações do esporte e atualizar o objeto de esportes
        self.fetchSportInfo = function (sport) {
            if (!sport.Id) {
                console.error("Invalid sport ID:", sport);
                return;
            }

            $.ajax({
                url: self.sportAPI + sport.Id,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados do esporte recebidos:", data);

                    // Add default values for missing data
                    sport.pictogram = data.Pictogram || 'default-pictogram.png';
                    sport.sportUrl = data.Sport_url || '#';
                    sport.link = `atletismo.html?id=${sport.Id}`;

                    // Add the sport to the list and notify Knockout
                    self.venueInfo().sports.push(sport);
                    self.venueInfo.valueHasMutated();
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar informações do esporte: ${textStatus} - ${errorThrown}`);
                    console.error("Detalhes do erro:", jqXHR.responseText);
                }
            });
        };

        // Função para buscar informações do tempo
        self.fetchWeatherInfo = function (lat, lon) {
            const weatherAPI = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${OPENWEATHERMAP_API_KEY}&units=metric`;

            $.ajax({
                url: weatherAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Dados do tempo recebidos:", data);

                    // Atualiza os dados do tempo no observable
                    self.venueInfo().weather = {
                        temperature: data.main.temp,
                        description: data.weather[0].description,
                        icon: `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`
                    };
                    self.venueInfo.valueHasMutated();
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Erro ao buscar informações do tempo: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Inicializa a busca
        self.fetchVenueInfo();
    }

    // Cria e aplica o ViewModel
    var vm = new VM();
    ko.applyBindings(vm);
});