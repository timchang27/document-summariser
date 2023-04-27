import React from 'react'

const Summary = ({responseData}) => {
    return (
        <div>
            <h2>Summary</h2>
            {responseData && responseData.answer && (
                <p>{responseData.answer}</p>
            )}
        </div>
    )
}

export default Summary