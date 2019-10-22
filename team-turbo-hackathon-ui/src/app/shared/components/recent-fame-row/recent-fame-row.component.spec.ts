import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentFameRowComponent } from './recent-fame-row.component';

describe('RecentFameRowComponent', () => {
  let component: RecentFameRowComponent;
  let fixture: ComponentFixture<RecentFameRowComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecentFameRowComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecentFameRowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
