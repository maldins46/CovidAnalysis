import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DesktopMenuItemIconComponent } from './desktop-menu-item-icon.component';

describe('IconMenuItemComponent', () => {
  let component: DesktopMenuItemIconComponent;
  let fixture: ComponentFixture<DesktopMenuItemIconComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DesktopMenuItemIconComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DesktopMenuItemIconComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
