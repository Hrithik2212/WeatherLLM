import React from "react";



const ContentWrapper = ({ children,className }) => {
    return <div className={`w-full max-w-[1600px]  mx-auto ${className}`}>{children}</div>;
};

export default ContentWrapper;