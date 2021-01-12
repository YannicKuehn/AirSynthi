// Animations init
// new WOW().init();

let sliders = document.getElementsByClassName("form-range");
let reverbOutput = document.getElementById("reverbOutput");
let filterOutput = document.getElementById("filterOutput");
let reverbList = document.querySelector("#btn-group-reverb");
let filterList = document.querySelector("#btn-group-filter");


for (let i = 0; i < sliders.length; i++) {
    sliders[i].addEventListener("input", changeParameter)
}

function changeParameter() {
    switch (this.id) {
        case "distortionSlider":
            // distortion.curve = makeDistortionCurve(this.value);
            document.querySelector("#distortionOutput").innerHTML = this.value;
            break;
        case "lfoSlider":
            // lfo.frequency.value = this.value;
            document.querySelector("#lfoOutput").innerHTML = this.value + " HZ";
            break;
            // Compressor Slider
        case "attackSlider":
            // attack = (this.value / 100);
            document.querySelector("#attackOutput").innerHTML = (this.value / 100) + " sec";
            document.querySelector("#attackOutput").inner
            break;
        case "releaseSlider":
            // release = (this.value / 100);
            document.querySelector("#releaseOutput").innerHTML = (this.value / 100) + " sec";
            break;
            // Filter Slider
        case "frequencySlider":
            // filter.frequency.value = (this.value);
            document.querySelector("#frequencyOutput").innerHTML = (this.value) + " Hz";
            break;
        case "detuneSlider":
            // filter.detune.value = (this.value);
            document.querySelector("#detuneOutput").innerHTML = (this.value) + " cents";
            break;
        case "qSlider":
            // filter.Q.value = (this.value);
            document.querySelector("#qOutput").innerHTML = (this.value) + " ";
            break;
        case "gainSlider":
            // filter.gain.value = (this.value);
            document.querySelector("#gainOutput").innerHTML = (this.value) + " db";
            break;
    }
}

let reverbButtons = ["room", "garage", "church", "cave"];
let filterButtons = ["#lowpass", "#highpass", "#bandpass", "#allpass", "#lowshelf", "#Highshelf", "#peaking", "#notch"];


reverbList.addEventListener("mousedown", function (e) {
    let name = e.target.value;
    reverbOutput.innerHTML = name;
    // if ()
    changeActiveButtonClass(name, reverbButtons);

    // loadImpulseResponse(name);
});


filterList.addEventListener("mousedown", function (e) {
    let name = e.target.value;
    filterOutput.innerHTML = name;

    changeActiveButtonClass(name, filterButtons);
});


function changeActiveButtonClass(name, buttonList) {
    buttonList = buttonList;
    element = document.getElementById(name);
    
    for (r in buttonList) {
        document.getElementById(buttonList[r]).classList.remove("active");
    }
    
    element.classList.add("active");
}


// distortion.curve = makeDistortionCurve(0);
// distortion.oversample = "4x";

// function makeDistortionCurve(amount) {
//     let n_samples = 44100,
//         curve = new Float32Array(n_samples);

//     for (let i = 0; i < n_samples; ++i) {
//         let x = i * 2 / n_samples - 1;
//         curve[i] = (Math.PI + amount) * x / (Math.PI + (amount * Math.abs(x)));
//     }

//     return curve;
// };