import { Component, OnInit } from '@angular/core';
import { UserService } from '../shared/services/user.service';
import { Users } from '../shared/models/users';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  users: Users[];

  constructor(
    private userService: UserService
  ) { }

  ngOnInit() {
    this.userService.getAllUsers().subscribe(result => {
      this.users = result;
    });
  }

}
