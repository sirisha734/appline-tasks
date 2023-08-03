import React from 'react';
import { useNavigate, useLocation} from 'react-router-dom';
import './ViewCard.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faClock, faHourglassHalf } from "@fortawesome/free-solid-svg-icons";

function ViewCard(){
    const navigate = useNavigate();
    const location = useLocation();

    const goSource = () => {
        navigate(-1);
    };

    const pri = location.state.priority_level

    return(
        <>
            <div className="task-card">
            <div id="view-card" className="card shadow p-3 mb-5 bg-white rounded">
              <div className="card-body">
                <h3 className="card-title">{location.state.task_name}</h3>
                <p>{location.state.description}</p>
                <p><FontAwesomeIcon icon={faClock} />&nbsp;{location.state.assigned_date}</p>
                <p><FontAwesomeIcon icon={faHourglassHalf} />&nbsp;{location.state.due_date}</p>
                <h5 style={{color: pri === "high" ? "#d10000" :  (pri === "medium" ? "#ffbf00" : "green")}}>
                    {location.state.priority_level}
                </h5>
              </div>
            </div>
            <button type="button" className="btn btn-light"
                  style={{
                    backgroundColor: "var(--primary-color)",
                    color: "white"
                  }}
                  onClick={goSource}
            >Go Back</button>
            </div>
        </>
    );
}

export default ViewCard;