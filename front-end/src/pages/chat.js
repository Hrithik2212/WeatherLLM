import React, { useEffect, useState, useRef } from 'react';
import { IoSend } from 'react-icons/io5';
import { AiOutlineLoading3Quarters } from 'react-icons/ai';
import { BASE_API } from '../utils/api';

const Chat = () => {
    const [message, setMessage] = useState('');
    const [userMessages, setUserMessages] = useState([]);
    const [botMessages, setBotMessages] = useState([]);
    const [loading, updateLoading] = useState(false);
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
    }, [botMessages, userMessages, loading]);

    function formatApiResponse(apiResponse) {
        let formattedResponse = apiResponse.replace(/\n/g, '<br>');
        formattedResponse = formattedResponse.replace(/\t/g, '&nbsp;&nbsp;&nbsp;');
        formattedResponse = formattedResponse.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        return formattedResponse;
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        setUserMessages([...userMessages, event.target.elements.userQuery.value]);
        setMessage("");
        
        const fetchResponse = async () => {
            updateLoading(true);
            try {
                const url = `${BASE_API}/post_query`;
                const requestBody = {
                    query: event.target.elements.userQuery.value,
                    default_city: 'chennai', // Set a default city or get it from user input
                    widget_city: 'widget_city' // Set a widget city or get it from user input
                };

                const res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestBody)
                });

                const response = await res.json();
                if (res.ok) {
                    const value = formatApiResponse(response.response);
                    setBotMessages([...botMessages, { response: value }]);
                } else {
                    throw new Error(response.error);
                }
            } catch (error) {
                setBotMessages([...botMessages, { response: 'Unable to load' }]);
            }
            updateLoading(false);
        };

        fetchResponse();
    };

    return (
        <div className='overflow-hidden '>
            <div className='flex h-screen'>
                <div className='bg-[#160042] w-[30%] flex justify-center items-center h-full max-md:hidden'>
                    <div className='flex h-full w-full flex-cols justify-center items-center'>
                        <h1 className='text-[40px] text-white font-bold max-md:text-[20px] text-center'>Weather Assistant Bot</h1>
                    </div>
                </div>
                <div className='bg-[#b4c6d0] min-h-[90%] flex w-[70%] max-md:w-full relative justify-center h-full'>
                    <div ref={scrollContainerRef} className='overflow-y-scroll transform transition-all ease-in-out duration-500 max-h-screen py-20 hide-scrollbar max-md:w-full sm:w-[900px] md:w-[90%] 2xl:w-[70%]'>
                        <div className='mb-5'>
                            <div className='bot-input-bg bg-transparent'>
                                <div className='bot-input-wrapper w-[90%] md:w-[70%]'>
                                    <h1 className='m-3'>Hi, I am your Weather Assistant , how may I help you.</h1><br />
                                </div>
                            </div>
                            {userMessages.map((e, key) =>
                                <div key={key} className='w-full'>
                                    <div className='user-input-bg'>
                                        <div className='user-input-wrapper bg-[#2e373b] text-white w-[90%] md:w-[70%]'>
                                            <h1 className='m-3 break-all'>{e}</h1><br />
                                        </div>
                                    </div>
                                    {botMessages[key] != null &&
                                        <div className='bot-input-bg bg-transparent'>
                                            <div className='bot-input-wrapper w-[90%] md:w-[70%]' dangerouslySetInnerHTML={{ __html: (botMessages[key].response) }} />
                                        </div>
                                    }
                                </div>
                            )}
                            {loading && <div className='flex justify-center'><li className='text-white text-[15px] floating dot1'/><li className='text-green-500 text-[15px] floating dot2'/><li className='text-yellow-500 text-[15px] floating dot3'/></div>}
                        </div>
                    </div>
                    <div className="fixed bottom-5 w-full">
                        <div className="flex justify-center">
                            <form onSubmit={handleSubmit} method='post' className='relative'>
                                <input
                                    name='userQuery'
                                    id="userQuery"
                                    className="max-md:w-[350px] md:w-[450px] lg:w-[600px] bg-[#1e2f36] text-white flex p-3 outline-none border-none justify-center max-h-[350px] pr-[10%]"
                                    placeholder="Type your message..."
                                    value={message}
                                    autoComplete='off'
                                    onChange={handleInputChange}
                                    required
                                />
                                {!loading && <button type='submit' className='absolute bottom-[1%] pointer bg-[#160042] p-1 rounded-lg m-2 right-0 text-white'><IoSend size={30}/></button>}
                                {loading && <div className='absolute bottom-[1%] bg-[#477590] p-1 rounded-lg m-2 right-0 text-white'><AiOutlineLoading3Quarters className='loading-spinner' size={30}/></div>}
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Chat;
