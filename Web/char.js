const canvas = document.getElementById("canva");
const width = (canvas.width = window.innerWidth);
const height = (canvas.height = window.innerHeight);
const ctx = canvas.getContext("2d");

const points = [
    {x: 0, y: 262},
    {x: 20, y: 254},
    {x: 60, y: 273}, 
    {x: 80, y: 106},
    {x: 88, y: 283},
    {x: 164, y: 209},
    {x: 216, y: 283},
];

let prev = null;
const xScale = 7;
const yScale = 3;
const pointRadious = 10;

points.forEach(point => {
    // draw
    if (prev != null) {
        ctx.beginPath();
        ctx.lineWidth = 15;
        ctx.moveTo(prev.x * xScale, prev.y * yScale);
        ctx.lineTo(point.x * xScale, point.y * yScale);
        ctx.stroke();
    }

    // save previous point
    prev = point;
});

points.forEach(point => {
    ctx.beginPath();
    ctx.arc(point.x * xScale, point.y * yScale, pointRadious, 0, 2 * Math.PI);
    ctx.fillStyle = "orange";
    ctx.fill(); 
});


