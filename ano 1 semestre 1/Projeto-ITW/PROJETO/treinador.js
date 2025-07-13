const coachId = new URLSearchParams(window.location.search).get("id");

$(document).ready(function () {
    function VM() {
        var self = this;

        // URL da API do Coach
        self.coachAPI = `http://192.168.160.58/Paris2024/api/Coaches/${coachId}`;

        // Observable to store coach information
        self.coachInfo = ko.observable({
            id: '',
            name: '',
            birthDate: '',
            sex: '',
            photo: '',
            function: '',
            country: '',
            sports: []  // List of associated sports
        });

        // Function to fetch coach details
        self.fetchCoachInfo = function () {
            if (!coachId) {
                console.error("Coach ID not found in the URL.");
                return;
            }

            $.ajax({
                url: self.coachAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Coach data received:", data);

                    // Update the coach information observable
                    self.coachInfo({
                        id: data.Id,
                        name: data.Name,
                        birthDate: data.BirthDate ? new Date(data.BirthDate).toLocaleDateString() : 'Unknown',
                        sex: data.Sex,
                        photo: data.Photo || '/PROJETO/imagens/PersonNotFound.png',
                        function: data.Function,
                        country: data.Country,
                        sports: data.Sports.map(sport => ({
                            id: sport.Id,
                            name: sport.Name
                        })) || []
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Error fetching coach information: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Initialize the fetch
        self.fetchCoachInfo();
    }

    // Apply Knockout bindings
    var vm = new VM();
    ko.applyBindings(vm);
});
