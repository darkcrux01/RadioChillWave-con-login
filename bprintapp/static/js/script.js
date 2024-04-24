const c = document.querySelector("canvas");
const radio_player = document.querySelector('#radio_player');

let opt = {
    width: c.offsetWidth,
    height: c.offsetHeight,
    midY: c.offsetHeight / 2,
    points: 80,
    stretch: 10,
    sinHeight: 0,
    speed: -0.1,
    strokeColor: 'violet',
    strokeWidth: 1.5,
    power: false,
};
c.width = opt.width *2;
c.height = opt.height *2;
c.style.width = opt.width;
c.style.height = opt.height;

const ctx = c.getContext ('2d');
ctx.scale(2,2);

ctx.strokeStyle = opt.strokeColor;
ctx.lineWidth = opt.strokeWidth;
ctx.lineCap = 'round';
ctx.lineJoin = 'round';

let time = 0;

const render = ()   => {
    window.requestAnimationFrame (render);
    ctx.clearRect(0,0, opt.width ,opt.height);
    time +=1;
    ctx.beginPath();
    let increment=0;

    for (i=0; i <= opt.points; i++){
        if (i < opt.points / 2){
            increment += 0.1;
        } else {
            increment += -0.1;
        }

        const x = (opt.width / opt.points) * i;
        const y = opt.midY + Math.sin (time * opt.speed + i / opt.stretch) * opt.sinHeight * increment ;

        ctx.lineTo (x,y);

    }   

    ctx.stroke();

}

render();
c.addEventListener('click', () =>  {
    opt.power = !opt.power;

    if (opt.power){
        radio_player.play();
        TweenMax.to(opt, 1, {
            sinHeight: 4,
            stretch: 5 ,
            ease: Power2.easeInOut,
        });
    }else {
        radio_player.pause();
        TweenMax.to(opt, 1,{
            sinHeight: 0,
            stretch: 10,
            ease: Power3.easeOut,
        });
    }
});