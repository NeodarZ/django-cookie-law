var Cookielaw = {

    createCookie: function (name, value, days) {
        var date = new Date(),
            expires = '';
        if (days) {
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toGMTString();
        } else {
            expires = "";
        }
        document.cookie = name + "=" + value + expires + "; path=/";
    },

    eraseCookie: function(name) {
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;';
    },

    getCookie: function(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1);
            if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
        }
        return "";
    },

    createCookielawCookie: function () {
        this.createCookie('cookielaw_accepted', '1', 1 * 365);

        document.getElementById('CookielawBanner').style.display = 'none';
    }

};

/* Js mode */
document.addEventListener("DOMContentLoaded", function(event) { 
    var el = document.querySelector("#CookielawBanner");
    if (el) {
        if (!Cookielaw.getCookie("cookielaw_accepted")) {
            el.style.display = "block";
        }
    }
});
