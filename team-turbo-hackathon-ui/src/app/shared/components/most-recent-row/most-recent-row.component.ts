import { UserWithPhoto } from './../../models/userWithPhoto';
import { Users } from './../../models/users';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ViewDetailsComponent } from '../modal/view-details/view-details.component';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-most-recent-row',
  templateUrl: './most-recent-row.component.html',
  styleUrls: ['./most-recent-row.component.scss']
})

export class MostRecentRowComponent implements OnInit {

  name: string;
  users: Users[];
  userWithPhotos: UserWithPhoto[] = [];
  shamedUsers: Users[];
  userIdList = [];

  constructor(
    public dialog: MatDialog,
    private userService: UserService
  ) { }


  ngOnInit() {
    this.userService.getAllUsers().subscribe(result => {
      this.shamedUsers = result.filter(s => s.status === '0');
      this.shamedUsers.map(user => {
        this.userService.addPhotosToUser(user.user_id).subscribe(photo => {
          let currentPhoto = photo;
          this.userWithPhotos.push(new UserWithPhoto(
            user.user_id,
            photo,
            this.convertHexToTime(user._id.$oid),
            user.firstName,
            user.lastName,
            user.los,
            user.lastUpdated
          ));
          this.userWithPhotos.sort(this.compare);
          console.log(this.userWithPhotos);
        });
      });
    });

  }

  compare(a, b) {
    if (a.lastUpdated === undefined) {
      a.lastUpdated = '0';
    }
    if (b.lastUpdated === undefined) {
      b.lastUpdated = '0';
    }
    if (a.lastUpdated < b.lastUpdated) {
      return 1;
    }
    if (a.lastUpdated > b.lastUpdated) {
      return -1;
    }
    return 0;
  }

  viewDetails(i) {
    let person = this.userWithPhotos[i];
    const dialogRef = this.dialog.open(ViewDetailsComponent, {
      width: '30%',
      data: {
        index: i,
        user_id: person.user_id,
        firstName: person.firstName,
        lastName: person.lastName,
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      this.userService.updateUser(result, person.user_id).subscribe();
      person.firstName = result.firstName;
      person.lastName = result.lastName;
    });
  }

  convertHexToTime(objectId) {
    return parseInt(objectId.substring(0, 8), 16);
  }

}
