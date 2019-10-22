import { ViewDetailsComponent } from './../modal/view-details/view-details.component';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';
import { UserService } from '../../services/user.service';
import { Users } from '../../models/users';

@Component({
  selector: 'app-recent-fame-row',
  templateUrl: './recent-fame-row.component.html',
  styleUrls: ['./recent-fame-row.component.scss']
})
export class RecentFameRowComponent implements OnInit {

  famedUsers: Users[];
  users: Users[];
  name: string;
  fakePhotoId: number;

  constructor(
    private dialog: MatDialog,
    private userService: UserService
  ) { }

  ngOnInit() {
    this.fakePhotoId = 0;
    this.userService.getAllUsers().subscribe(result => {
      this.famedUsers = result.filter(s => s.status === '1');
      // console.log(this.famedUsers);
    }

    );

    this.incrementPhotoId(this.fakePhotoId);

  }

  incrementPhotoId(id) {
    id++
  }

  viewDetails() {
    const dialogRef = this.dialog.open(ViewDetailsComponent, {
      width: '30%',
      data: { name: this.name }
    });

    dialogRef.afterClosed().subscribe(result => {
      // console.log('dialog closed, belive it.');
      this.name = result;
    });
  }

}
