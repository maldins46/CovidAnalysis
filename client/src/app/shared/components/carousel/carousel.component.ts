import {Component, Input, OnInit} from '@angular/core';
import {SlideModel} from '../../models/slide.model';

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.scss'],
})
export class CarouselComponent implements OnInit {
  @Input() slides: SlideModel[] = [];
  currentSlide = 0;


  constructor() { }

  ngOnInit(): void {
    this.preloadImages(); // for the demo
  }

  preloadImages(): void {
    for (const slide of this.slides) {
      new Image().src = slide.src;
    }
  }


  onPreviousClick(): void {
    const previous = this.currentSlide - 1;
    this.currentSlide = previous < 0 ? this.slides.length - 1 : previous;
  }

  onNextClick(): void {
    const next = this.currentSlide + 1;
    this.currentSlide = next === this.slides.length ? 0 : next;
  }
}
