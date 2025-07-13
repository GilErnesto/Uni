$(document).ready(function () {
    const nocId = new URLSearchParams(window.location.search).get("id");

    function ViewModel() {
        var self = this;

        // API URL
        self.nocAPI = `http://192.168.160.58/Paris2024/api/NOCs/${nocId}`;

        // Observables
        self.nocInfo = ko.observable({
            Id: '',
            Name: '',
            Note: '',
            Photo: '',
            Url: ''
        });
        self.athletes = ko.observableArray([]);
        self.coaches = ko.observableArray([]);
        self.medals = ko.observableArray([]);
        self.teams = ko.observableArray([]);

        // Log Helper
        self.log = function (message) {
            console.log(`[ViewModel Log]: ${message}`);
        };

        // Fetch NOC info from API
        self.fetchNocInfo = function () {
            self.log("Fetching NOC info...");
            $.ajax({
                url: self.nocAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    self.log("NOC info fetched successfully.");
                    console.log("API Response:", data);

                    // Update general NOC info
                    self.nocInfo({
                        Id: data.Id,
                        Name: data.Name,
                        Note: data.Note,
                        Photo: data.Photo,
                        Url: data.Url
                    });

                    // Update athletes
                    if (data.Athletes && Array.isArray(data.Athletes)) {
                        self.athletes(data.Athletes);
                    }

                    // Update coaches
                    if (data.Coaches && Array.isArray(data.Coaches)) {
                        self.coaches(data.Coaches);
                    }

                    // Update medals
                    if (data.Medals && Array.isArray(data.Medals)) {
                        self.medals(data.Medals);
                    }

                    // Update teams
                    if (data.Teams && Array.isArray(data.Teams)) {
                        self.teams(data.Teams);
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    self.log(`Error fetching NOC info: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Initialize fetch
        self.fetchNocInfo();
    }

    // Apply bindings
    var vm = new ViewModel();
    ko.applyBindings(vm);
});