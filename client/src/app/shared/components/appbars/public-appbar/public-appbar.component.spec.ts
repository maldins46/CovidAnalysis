import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PublicAppbarComponent } from './public-appbar.component';

describe('PublicAppbarComponent', () => {
  let component: PublicAppbarComponent;
  let fixture: ComponentFixture<PublicAppbarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PublicAppbarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PublicAppbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
