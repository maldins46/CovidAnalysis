import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrivacyPolicySnackbarComponent } from './privacy-policy-snackbar.component';

describe('PrivacyPolicySnackbarComponent', () => {
  let component: PrivacyPolicySnackbarComponent;
  let fixture: ComponentFixture<PrivacyPolicySnackbarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PrivacyPolicySnackbarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PrivacyPolicySnackbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
