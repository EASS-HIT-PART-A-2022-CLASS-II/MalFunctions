import { HttpClient } from '@angular/common/http';
import { Component, ViewChild } from '@angular/core';
import { DxDataGridComponent } from 'devextreme-angular';
import notify from 'devextreme/ui/notify';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {


  @ViewChild('gridContainer', { static: false }) dataGrid!: DxDataGridComponent;

  constructor(
    private http: HttpClient,

  ) { }

  newMalList: any;

  ngOnInit() {
    this.http.get("http://localhost:8080/check").subscribe(res => {

      console.log("result from check:", res);
      if (res == "exists" || res == "created") {
        notify("Database approved, ready for work", 'success', 3000);
        this.http.get("http://localhost:8080/getList").subscribe(res => {
          console.log("Result: ", res);
          this.newMalList = res;
        }, err => {
          notify("Error, cannot get malfunction list", 'success', 3000);
        });
      }


    }, err => {
      notify("Error, cannot approve database", 'error', 3000);
    });
  }


  title = 'frontend';

  completed:any = []
  statusTypes = [
    { id: 1, status: "Pending", color:"#bee0ec"},
    { id: 2, status: "In Progress", color: "orange"},
    { id: 3, status: "Completed", color: "#aee5a8" },
  ]
  new = [
    { id: 1, description:"fix toilet", creator: "roman", date: Date.now(), status: 1 },
    { id: 2, description: "fix bathroom", creator: "dani", date: Date.now(), status: 1 },
    { id: 3, description: "fix toilet", creator: "roman", date: Date.now(), status: 2 },
    { id: 4, description: "fix toilet", creator: "roman", date: Date.now(), status: 1 },
    { id: 5, description: "fix toilet", creator: "roman", date: Date.now(), status: 1 },
    { id: 6, description: "fix toilet", creator: "roman", date: Date.now(), status: 2 },
    { id: 7, description: "fix toilet", creator: "roman", date: Date.now(), status: 1 },
    { id: 8, description: "fix toilet", creator: "roman", date: Date.now(), status: 1 },
  ]

  insertRow(e: any) {
    e.data.status = 1;
    e.data.date = Date.now();;
  }

  onRowInserted(e: any) {
    let obj = {
      id: 0,
      description: e.data.description,
      creator: e.data.creator,
      date: e.data.date,
      status: e.data.status
    };
    this.http.post("http://localhost:8080/addMal", obj).subscribe(res => {
      console.log("backFrom sql: ", res);
      this.dataGrid.instance.refresh()
    });
  }
  onRowRemoved(e: any) {
    console.log("delete id: ", e.data.id);
  } 


  RowUpdated(e: any) {
    if (e.data.status == 3) {
      let obj = this.new.find((obj: any) => obj.id === e.data.id);
      this.completed.push(obj);
      this.new = this.new.filter(item => item.id !== e.data.id);
    }
  }
  onRowPrepared(e: any) {
    if (e.rowType === "data") {
      let obj = this.statusTypes.find((obj: any) => obj.id === e.data.status);
      e.rowElement.bgColor = obj?.color; //set the background color based on the data
    }
    if (e.rowType === "header") {
      e.rowElement.bgColor = "#cacbca"; //set the background color based on the data
    }

  }
  GetMals() {
    this.http.get("http://localhost:8080/getList").subscribe(res => {
      console.log("Result: ", res);
    });
  }
}
