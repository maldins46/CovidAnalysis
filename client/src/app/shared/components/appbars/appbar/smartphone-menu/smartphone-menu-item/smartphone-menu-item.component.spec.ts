import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmartphoneMenuItemComponent } from './smartphone-menu-item.component';

describe('SmartphoneMenuItemComponent', () => {
  let component: SmartphoneMenuItemComponent;
  let fixture: ComponentFixture<SmartphoneMenuItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SmartphoneMenuItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SmartphoneMenuItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
