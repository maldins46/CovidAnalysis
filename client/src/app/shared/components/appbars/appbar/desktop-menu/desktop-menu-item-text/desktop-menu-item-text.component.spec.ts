import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DesktopMenuItemTextComponent } from './desktop-menu-item-text.component';

describe('TextMenuItemComponent', () => {
  let component: DesktopMenuItemTextComponent;
  let fixture: ComponentFixture<DesktopMenuItemTextComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DesktopMenuItemTextComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DesktopMenuItemTextComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
