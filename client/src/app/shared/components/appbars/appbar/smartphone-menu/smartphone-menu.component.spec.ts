import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmartphoneMenuComponent } from './smartphone-menu.component';

describe('SmartphoneMenuComponent', () => {
  let component: SmartphoneMenuComponent;
  let fixture: ComponentFixture<SmartphoneMenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SmartphoneMenuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SmartphoneMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
