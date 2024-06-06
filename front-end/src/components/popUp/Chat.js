import React,{useState,useEffect,useRef} from 'react'
import {BASE_API} from '../../utils/api'
import { IoCloseSharp } from "react-icons/io5";


const Chat = ({setShowChat}) => {
        const [message, setMessage] = useState(''); 
        const [userMessages,setUserMessages]=useState([])
        const [BotMessages,setBotMessages]=useState([])
        const [loading,updateLoding]=useState(false)
        const scrollContainerRef = useRef(null);

        const handleInputChange = (event) => {          
                const { value } = event.target;
                setMessage(value);

    };
    const scrollToBottom = () => {
    
        if (scrollContainerRef.current) {
        const scrollHeight = scrollContainerRef.current.scrollHeight;
        const height = scrollContainerRef.current.clientHeight;
        scrollContainerRef.current.scrollTop = scrollHeight - height;
        }
    };

    useEffect(() => {
        scrollToBottom();
        
      }, [BotMessages,userMessages,loading]);
      function formatApiResponse(apiResponse) {
        let formattedResponse = apiResponse.replace(/\n/g, '<br>');
        formattedResponse = formattedResponse.replace(/\t/g, '&nbsp;&nbsp;&nbsp;');
        formattedResponse = formattedResponse.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        return formattedResponse;
      }
    
    
      const handelSubmit= (event)=>{
        event.preventDefault()
        
        setUserMessages([...userMessages,event.target.elements.userquerry.value])
        
        setMessage("");
        const fetchResponse = async () =>{
            updateLoding(true)
            try{
              var url=`${BASE_API}/api/getres/?question=${encodeURIComponent(event.target.elements.userquerry.value)}/`;
              const res= await fetch(url)
              const response = await res.json()
              if(res.ok){
                const value= await formatApiResponse(response.response)
                setBotMessages([...BotMessages,{"response":value}])
              }else{
                throw res.error
              }
              
            }
            catch{
              setBotMessages([...BotMessages,{"response":"unable to load"}])
    
              
            }
           
            updateLoding(false)
              
        }
        fetchResponse()
        
      }
  return (
    <main className='fixed my-font right-0  lg:w-[50%] max-sm:w-full  md:w-[80%] max-md:w-[90%] flex   items-center justify-center sm:items-end sm:justify-end   z-[100] bottom-0'>
            <section className=" flex flex-col items-center justify-center max-sm:w-[95%] sm:items-end sm:justify-end  min-h-[30rem] h-[30vw] sm:w-[80%]  text-gray-800 sm:px-10">

                

                <div className="flex flex-col flex-grow w-full max-w-xl bg-gray-200 max-sm:w-full shadow-xl rounded-lg overflow-hidden">
                <div className='p-2 flex w-full justify-end'><IoCloseSharp size={30} onClick={()=>{setShowChat(false)}}/></div>
                    <div ref={scrollContainerRef} className="flex flex-col items-center flex-grow h-0 p-2 overflow-auto">

                        <div className="flex items-center justify-end space-x-3  mt-1  w-full">
                                <div className="flex flex-col justify-end items-end gap-2 p-2">

                                    <div  className='space-x-3 p-3 rounded-r-lg   rounded-bl-lg ' >
                                            <div>  
                                                        <h1 className='text-black'>Hi , I am your virtual leave application assitant , I am here to help you with information about leave types and eligibility criteria. Feel free to ask any queries</h1><br/>   
                                            </div> 
                                    </div>
                                       
                                    
                                        {userMessages.map((e,key)=>
                                            <div key={key} className=' w-full    flex flex-col justify-end items-end gap-2'>
                                                        <div className='bg-blue-600 space-x-3 text-white ml-auto justify-end max-w-xs p-3 rounded-r-lg rounded-bl-lg'>  
                                                                    <h1 className='break-all text-sm'>{e}</h1>   
                                                        </div>
                                                        {BotMessages[key]!=null && 
                                                        <div className="space-x-3 p-3 rounded-r-lg   rounded-bl-lg ">
                                                            <div className=' ' dangerouslySetInnerHTML={{ __html: (BotMessages[key].response) }} />
        
                                                        </div>}
                                            </div>
                                  
                                      )}
                                      {loading && <div className='flex justify-center'><li className='text-white text-[15px] floating dot1'/><li className='text-green-500 text-[15px] floating dot2'/><li className='text-yellow-500 text-[15px] floating dot3'/></div>}
                             
                 
                                  
                                </div>
                        </div>
                        
                        
                        

                    </div>
                    
                    <div className="bg-gray-300 p-4">
                      <form onSubmit={handelSubmit}>
                            <input name='userquerry' id="userquerry" placeholder="Type your message..." value={message} autoComplete='off' onChange={handleInputChange}  className="flex items-center h-10 w-full rounded px-3 text-sm" type="text" />
                      </form>
                    </div>
                </div>

            </section>
      </main>
            
      
  )
}

export default Chat