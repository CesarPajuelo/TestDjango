class fetchWeatherApi {
    constructor() {
        this.baseApiUrl = 'https://www.metaweather.com/api/location';
        this.searchApiUrl = `${this.baseApiUrl}/search`;
        this.addCorsHeader();
    }

    addCorsHeader() {
        $.ajaxPrefilter(options => {
            if (options.crossDomain && $.support.cors) {
                options.url = 'https://the-ultimate-api-challenge.herokuapp.com/' + options.url;
            }
        });
    }

    getLocation(query, callback) {
        $.getJSON(this.searchApiUrl, { query })
            .done(data => callback(data))
            .fail(() => callback(null));
    }

    getWeatherData(location, callback) {
        $.getJSON(`${this.baseApiUrl}/${location}`)
            .done(data => callback(data))
            .fail(() => callback(null));
    }
}

class DomElements {
    constructor() {
        this.searchForm = $('#search-form');
        this.errorBox = $('#error-box');
        this.searchBox = $('#search-box');
        this.weatherBox = $('#weather-box');
    }

    showWeather() {
        this.hideError();
        this.weatherBox.removeClass('d-none');
        this.weatherBox.addClass('d-flex');
    }

    showSearch() {
        this.searchBox.removeClass('d-none');
        this.searchBox.addClass('d-flex');
    }

    hideSearchBox() {
        this.searchBox.removeClass('d-flex');
        this.searchBox.addClass('d-none');
    }

    showError(message) {
        this.showSearch();
        this.errorBox.removeClass('d-none');
        this.errorBox.addClass('d-block');
        this.errorBox.html(`<p class="mb-0">${message}</p>`);
    }

    hideError() {
        this.errorBox.addClass('d-none');
    }
}

class displayWeather {
    constructor() {
        this.imageURL = 'https://www.metaweather.com/static/img/weather';
    }
    showTodaysWeatherDetails({ name, value, unit }) {
        $(`#weather-details`).append(`
            <div class="d-flex justify-content-between">
                <span class="font-weight-bolder">${name}</span>
                <span>${value} ${unit}</span>
            </div>
        `);
    }
    showTodaysWeather(weather) {
        $('#weather-card-weekday').html(weather.currentWeekday);
        $('#weather-card-date').html(weather.todaysFullDate);
        $('#weather-card-location').html(weather.locationName);
        $('#weather-card-img').attr('src', `${this.imageURL}/${weather.todaysImgUrl}.svg`);
        $('#weather-card-temp').html(weather.todaysTemp);
        $('#weather-card-description').html(weather.weatherState);
    }
    
}

class dataMiddleware {
    constructor() {
        this.displayWeather = new displayWeather();
        this.DomElements = new DomElements();
    }
  

    gatherTodaysWeatherGeneral(data) {
        return {
            currentWeekday: moment(data.applicable_date).format('dddd'),
            todaysFullDate: moment(data.applicable_date).format('MMMM Do'),
            locationName: data.title,
            todaysImgUrl: data.weather_state_abbr,
            todaysTemp: Math.round(data.the_temp),
            weatherState: data.weather_state_name,
        };
    }

    prepareDataForDom(data) {
        const {    
            applicable_date,
            the_temp,
            weather_state_abbr,
            weather_state_name,
        } = data.consolidated_weather[0];

        const todaysWeatherGeneral = this.gatherTodaysWeatherGeneral({
            applicable_date,
            weather_state_abbr,
            weather_state_name,
            the_temp,
            title: data.title,
        });
       

        this.DomElements.showWeather();
        this.displayWeather.showTodaysWeather(todaysWeatherGeneral);
    }

    prepareTodaysWeatherDetails(Weather) {
        $.each(Weather, (key, value) => {
            this.displayWeather.showTodaysWeatherDetails({
                name: key.toUpperCase(),
                value: value.value,
                unit: value.unit,
            });
        });
    }

  
}
class requestController {
    constructor() {
        this.fetchWeatherApi = new fetchWeatherApi();
        this.DomElements = new DomElements();
        this.dataMiddleware = new dataMiddleware();
        this.registerEventListener();
    }

    showRequestInProgress() {
        this.DomElements.hideSearchBox();
    }

    getQuery() {
        return $('#search-query').val().trim();
    }

    fetchWeather(query) {
        this.fetchWeatherApi.getLocation(query, location => {
            if (!location || location.length === 0) {
                this.DomElements.showError('No se puede encontrar la capital, verifique si esta escrito en ingles.');
                return;
            }

            this.fetchWeatherApi.getWeatherData(location[0].woeid, data => {
                if (!data) {
                    this.DomElements.showError('Por favor intente Despues.');
                    return;
                }

                this.dataMiddleware.prepareDataForDom(data);
            });
        });
    }

    onSubmit() {
        const query = this.getQuery();
        if (!query) return;

        this.fetchWeather(query);
    }

    registerEventListener() {
        this.DomElements.searchForm.on('submit', e => {
            e.preventDefault();
            this.onSubmit();
        });
    }
}

const request = new requestController();