const modalityId = new URLSearchParams(window.location.search).get("id");

$(document).ready(function () {
    function VM() {
        var self = this;

        // API URL
        self.sportAPI = `http://192.168.160.58/Paris2024/api/Sports/${modalityId}`;

        // Observables
        self.sportInfo = ko.observable({
            id: '',
            name: '',
            url: '',
            pictogram: ''
        });
        self.athletes = ko.observableArray([]);
        self.athleteCount = ko.observable(0);
        self.teams = ko.observableArray([]);
        self.teamCount = ko.observable(0);
        self.coaches = ko.observableArray([]);
        self.coachCount = ko.observable(0);
        self.venues = ko.observableArray([]);
        self.venueCount = ko.observable(0);
        self.competitions = ko.observableArray([]);
        self.competitionCount = ko.observable(0);
        self.technicalOfficials = ko.observableArray([]);
        self.technicalOfficialCount = ko.observable(0);

        // Log Helper
        self.log = function (message) {
            console.log(`[VM Log]: ${message}`);
        };

        // Fetch sport info from API
        self.fetchSportInfo = function () {
            self.log("Fetching sport info...");
            $.ajax({
                url: self.sportAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    self.log("Sport info fetched successfully.");
                    console.log("API Response:", data);

                    // Update general sport info
                    self.sportInfo({
                        id: data.Id,
                        name: data.Name,
                        url: data.Sport_url,
                        pictogram: data.Pictogram
                    });

                    // Update athletes
                    if (data.Athletes && Array.isArray(data.Athletes)) {
                        self.athletes(data.Athletes);
                        self.athleteCount(data.Athletes.length);
                    }

                    // Update teams
                    if (data.Teams && Array.isArray(data.Teams)) {
                        self.teams(data.Teams);
                        self.teamCount(data.Teams.length);
                    } else {
                        self.teams([]);
                        self.teamCount(0);
                    }

                    // Update coaches
                    if (data.Coaches && Array.isArray(data.Coaches)) {
                        self.coaches(data.Coaches);
                        self.coachCount(data.Coaches.length);
                    } else {
                        self.coaches([]);
                        self.coachCount(0);
                    }

                    // Update venues
                    if (data.Venues && Array.isArray(data.Venues)) {
                        self.venues(data.Venues);
                        self.venueCount(data.Venues.length);
                    }

                    // Update competitions
                    if (data.Competitions && Array.isArray(data.Competitions)) {
                        const competitionsWithSportId = data.Competitions.map((comp, index) => ({
                            SportId: comp.SportId || "N/A", // Adiciona um valor padrão se SportId for indefinido
                            Name: comp.Name,
                            Tag: comp.Tag,
                            Id: comp.SportId + '_' + index  // Gera um Id único baseado em SportId e índice
                        }));

                        self.competitions(competitionsWithSportId);
                        self.competitionCount(competitionsWithSportId.length);
                    } else {
                        self.competitions([]);
                        self.competitionCount(0);
                    }

                    // Update technical officials
                    if (data.Technical_officials && Array.isArray(data.Technical_officials)) {
                        self.technicalOfficials(data.Technical_officials);
                        self.technicalOfficialCount(data.Technical_officials.length);
                    } else {
                        self.technicalOfficials([]);
                        self.technicalOfficialCount(0);
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    self.log(`Error fetching sport info: ${textStatus} - ${errorThrown}`);
                }
            });
        };

        // Initialize fetch
        self.fetchSportInfo();
    }

    // Apply bindings
    var vm = new VM();
    ko.applyBindings(vm);
});
