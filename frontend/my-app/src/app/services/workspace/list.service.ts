import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { List } from './../../Interfaces/List';

const httpOptions = {
  headers: new HttpHeaders({}),
};

@Injectable({
  providedIn: 'root',
})
export class ListService {
  private apiURL = 'http://37.32.13.83:8000/workspace/list';

  constructor(private http: HttpClient) {}

  createList(list: List): Observable<any> {
    const url = `${this.apiURL}/create`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    return this.http.post(url, list, httpOptions);
  }

  getLists(boardId: number): Observable<any> {
    const url = `${this.apiURL}/list?board_id=${boardId}`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    return this.http.get(url, httpOptions);
  }
}
