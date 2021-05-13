import {AfterViewInit, Component, ElementRef, Renderer2} from '@angular/core';

@Component({
  selector: 'app-twitter-feed',
  templateUrl: './twitter-feed.component.html',
  styleUrls: ['./twitter-feed.component.scss']
})
export class TwitterFeedComponent implements AfterViewInit {

  constructor(private renderer2: Renderer2, private el: ElementRef) {}

  ngAfterViewInit(): void {
    const scriptEl = document.createElement('script');
    scriptEl.src = 'https://platform.twitter.com/widgets.js';
    this.renderer2.appendChild(this.el.nativeElement, scriptEl);
  }
}
