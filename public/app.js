const firebaseConfig = {
    apiKey: "",
    authDomain: "",
    databaseURL: "",
    projectId: "",
    storageBucket: "",
    messagingSenderId: "",
    appId: "",
    measurementId: ""
};

firebase.initializeApp(firebaseConfig);

$("#flip").on("click", e => {
    let count = -1;
    firebase.database().ref("action").once("value").then(data => {
        count = data.val()["value"];
        let info = {};
        firebase.database().ref("action").update({value:count+1});
        info[String(count+1)] = 1;
        firebase.database().ref("action").update(info).then(e => {
            window.location = "results.html";
        });
    });
});

$("#no_flip").on("click", e => {
    let count = -1;
    firebase.database().ref("action").once("value").then(data => {
        count = data.val()["value"];
        let info = {};
        firebase.database().ref("action").update({value:count+1});
        info[String(count+1)] = 0;
        firebase.database().ref("action").update(info).then(e => {
            window.location = "results.html";
        });
    });
});
