$(document).ready(function () {
    function ViewModel() {
        var self = this;

        // Extract team ID from the URL
        const teamId = new URLSearchParams(window.location.search).get("id");

        if (!teamId) {
            console.error("Team ID not found in the URL.");
            return;
        }

        self.teamAPI = `http://192.168.160.58/Paris2024/api/Teams/${teamId}`;

        // Define observables for each property
        self.id = ko.observable('');
        self.name = ko.observable('');
        self.sex = ko.observable('');
        self.numAthletes = ko.observable(0);
        self.numCoaches = ko.observable(0);
        self.athletes = ko.observableArray([]);
        self.coaches = ko.observableArray([]);
        self.noc = ko.observable({ id: '', name: '' });
        self.sport = ko.observable({ id: '', name: '' });
        self.medals = ko.observableArray([]);

        // Function to fetch team info from the API
        self.fetchTeamInfo = function () {
            console.log("Fetching team info from API:", self.teamAPI);

            $.ajax({
                url: self.teamAPI,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log("Team data received:", data);

                    // Safeguard against missing fields
                    self.id(data.Id || '');
                    self.name(data.Name || '');
                    self.sex(data.Sex || '');
                    self.numAthletes(data.Num_athletes || 0);
                    self.numCoaches(data.Num_coaches || 0);
                    self.athletes(data.Athletes || []);
                    self.coaches(data.Coaches || []);
                    self.noc({ id: data.NOC.Id || '', name: data.NOC.Name || '' });
                    self.sport({ id: data.Sport.Id || '', name: data.Sport.Name || '' });

                    // Process medals to convert Medal_Type to text
                    var processedMedals = data.Medals.map(function (medal) {
                        return {
                            ...medal,
                            medalTypeText: medal.Medal_Type === 1 ? 'Ouro' : medal.Medal_Type === 2 ? 'Prata' : medal.Medal_Type === 3 ? 'Bronze' : ''
                        };
                    });
                    self.medals(processedMedals);

                    console.log("Updated observables:", ko.toJS(self));
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(`Error fetching team information: ${textStatus} - ${errorThrown}`);
                    console.log("Response Text:", jqXHR.responseText);
                }
            });
        };

        // Fetch team info on initialization
        self.fetchTeamInfo();
    }

    try {
        const vm = new ViewModel();
        ko.applyBindings(vm);
        console.log("Knockout bindings applied successfully.");
    } catch (e) {
        console.error("Error applying Knockout bindings:", e);
    }
});