import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Users } from '../models/users';
import { Router } from '@angular/router';
import { UserWithPhoto } from '../models/userWithPhoto';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private http: HttpClient,
    private router: Router
  ) { }

  getAllUsers(): Observable<Users[]> {
    return this.http.get<Users[]>('http://3.16.47.17/users')
      .pipe(
        catchError(this.handleError<Users[]>('getAllUsers', []))
      );
  }

  getFakePhotos(): Observable<any> {
    return this.http.get<any>('https://jsonplaceholder.typicode.com/photos')
  }

  addPhotosToUser(userId: string): Observable<any> {
    return this.http.get<any>(`http://3.16.47.17:80/image/MattM`)
      .pipe(
        catchError(this.handleError<Users[]>('addPhotosToUser', []))
      );
  }

  addUser(user: Users): Observable<Users> {
    return this.http.post<Users>('http://3.16.47.17/users', user);
  }

  updateUser(user: UserWithPhoto, userId: string): Observable<Users> {
    return this.http.put<Users>(`http://3.16.47.17/users/${userId}`, user)
      .pipe(
        catchError(this.handleError<Users>('updateUser'))
      );
  }

  handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      // console.error(error);
      if (error.status === 403 || error.status === 404) {
        this.router.navigateByUrl('/error');
      }
      // console.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }
}
