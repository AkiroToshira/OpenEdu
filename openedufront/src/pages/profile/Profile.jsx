import './profile.css'
import profilePicture from '../../media/anime.jpeg'

import {ColorExtractor} from "react-color-extractor";
import {useState, useEffect, useContext} from "react";
import {useDispatch, useSelector} from "react-redux";
import {fetchProfile, fetchUserIdAndRole} from "../../actions/profile";

function Profile() {
  const dispatch = useDispatch()
  const user = useSelector(state => state.profile)
  const [userInfo, setUserInfo] = useState({
	first_name: "",
	last_name: '',
	email: ''
  })

  const [commonColor, setCommonColor] = useState()

  useEffect(() => {
	dispatch(fetchProfile())
  }, [])


  if (!user.loading) {
	return <div className="profile">
	  <div className="skew-block" style={{backgroundColor: `${commonColor}`, opacity: '0.4'}}/>
	  <div className="skew-block-bottom" style={{backgroundColor: `${commonColor}`, opacity: '0.3'}}/>
	  <ColorExtractor
		  src={profilePicture}
		  getColors={colors => setCommonColor(colors[0])}
	  />
	  <div className="profile-block">
		<div className="profile-title">
		  <h1><span>Профіль |</span> {user.first_name} {user.last_name}
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
			<p>{user.email}</p>
		  </div>
		</div>
	  </div>
	</div>
  } else {
	return <div>Loading...</div>
  }
}

export default Profile;