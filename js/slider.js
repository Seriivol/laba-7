$(document).ready(() =>{
let currentSlide=0;
let isBusy=false;

$('.slider-arrow').on('click',function(e){
	const slidesCount=slides.length-1;
	if(!isBusy){

		if($(this).hasClass('right')){
			currentSlide+=1;
			if (currentSlide>slidesCount)
				currentSlide=0;
		}
		else{
			currentSlide-=1;
			if(currentSlide<0)
				currentSlide=slidesCount;
		}
		isBusy=true;
		$('.slider-image').animate({'opasity':0},350,()=>{
			$('slider-image').css('background-image','url('+slides[currentSlide]+')');
			$('slider-image').animate({'opasity':1},350,()=>isBusy=false);
		});
	}
});
});
const slides=[
'img/img5.jpg',
'img/img6.jpg',
'img/img7.jpg',
'img/img8.jpg',
'img/img9.jpg',
'img/img10.jpg',
]