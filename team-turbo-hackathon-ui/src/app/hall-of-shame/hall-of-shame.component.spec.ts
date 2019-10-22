import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HallOfShameComponent } from './hall-of-shame.component';

describe('HallOfShameComponent', () => {
  let component: HallOfShameComponent;
  let fixture: ComponentFixture<HallOfShameComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HallOfShameComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HallOfShameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
