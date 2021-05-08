import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NotificationsToggleComponent } from './notifications-toggle.component';

describe('NotificationsToggleComponent', () => {
  let component: NotificationsToggleComponent;
  let fixture: ComponentFixture<NotificationsToggleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NotificationsToggleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NotificationsToggleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
