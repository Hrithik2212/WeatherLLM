import React, { useEffect, useState } from 'react'
import { RiCustomerService2Fill } from "react-icons/ri";
import Chat from './Chat';

const PopUp = () => {
    const [showChat,setShowChat] = useState(false)
    const [show,setShow]=useState(true)

    useEffect(()=>{
      setTimeout(()=>{
        setShow(false)
      },[4000])
    },[])
  return (
    <div className={`fixed ${showChat ? "bottom-0":"bottom-10"} max-md:  right-0`}>
        <div>
            {!showChat && 
                        <div onClick={()=>{setShowChat(true)}} className=' relative transform  transition-all ease-in-out duration-[2000ms] gap-3 bg-gray-200 rounded-full p-2 flex justify-center items-center text-center'>
                                <h1 className={`transform  transition-all ease-in-out duration-[2000ms]  ${!show && 'hidden translate-x-[120px] '}`}>Talk to me</h1>
                                <button><RiCustomerService2Fill size={40}/></button>
                        </div>
            }
        </div>
        <div>
            {showChat && 
            <div className=''>
              
              <Chat setShowChat={setShowChat}/>
              </div>}

        </div>
    </div>
  )
}

export default PopUp