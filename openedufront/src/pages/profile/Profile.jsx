import './profile.css'
import profilePicture from '../../media/anime.jpeg'
import {url} from '../../utils'

import {ColorExtractor} from "react-color-extractor";
import {useState, useEffect, useContext} from "react";
import axios from "axios";
import {Context} from "../../context";

function Profile() {
  const [commonColor, setCommonColor] = useState()
  const [state, dispatch] = useContext(Context)
  const [userInfo, setUserInfo] = useState({
	first_name: "",
	last_name: '',
	email: ''
  })

  useEffect(() => {
	axios.get(`${url}/user/${state.id}`, {
	  headers: {
		Authorization: 'JWT ' + state.access,
		'Content-Type': 'application/json'
	  }
	}).then(res => setUserInfo(res.data)
	)
  }, [state.isLogged])


  if (true) {
	return <div className="profile">
	  <div className="skew-block" style={{backgroundColor: `${commonColor}`, opacity: '0.4'}}/>
	  <div className="skew-block-bottom" style={{backgroundColor: `${commonColor}`, opacity: '0.3'}}/>
	  <ColorExtractor
		  src={profilePicture}
		  getColors={colors => setCommonColor(colors[0])}
	  />
	  <div className="profile-block">
		<div className="profile-title">
		  <h1><span>Профіль |</span> {userInfo.first_name} {userInfo.last_name}
			<div style={{
			  height: '5px',
			  width: '50%',
			  position: 'absolute',
			  borderRadius: '9999px',
			  bottom: '-20px',
			  left: '0',
			  backgroundColor: `${commonColor}`
			}}/>
		  </h1>

		</div>
		<div className="img-info-wrapper">
		  <div className="profile-img">
			<img src={profilePicture} alt={'profile'}/>
		  </div>
		  <div className="profile-info">
			<p>{userInfo.email}</p>

		  </div>
		</div>
	  </div>
	</div>
  } else {
	return <div>Loading</div>
  }
}

export default Profile;